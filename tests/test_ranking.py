import json
from datetime import UTC, datetime
from pathlib import Path

from pydantic import TypeAdapter

from auto_research_daily.config import load_config
from auto_research_daily.models import RawPaper, ZoteroDocument
from auto_research_daily.ranking import deduplicate_papers, rank_papers

ROOT = Path(__file__).parents[1]


def _fixture() -> tuple[list[RawPaper], list[ZoteroDocument]]:
    payload = json.loads((ROOT / "tests/fixtures/offline_daily.json").read_text(encoding="utf-8"))
    papers = TypeAdapter(list[RawPaper]).validate_python(payload["papers"])
    documents = TypeAdapter(list[ZoteroDocument]).validate_python(payload["zotero"])
    return papers, documents


def test_deduplicate_keeps_newer_version() -> None:
    papers, _ = _fixture()
    older = papers[0]
    newer = older.model_copy(update={"version": 2})
    result = deduplicate_papers([older, newer])
    assert len(result) == 1
    assert result[0].version == 2


def test_ranking_is_deterministic_and_explainable() -> None:
    config = load_config(ROOT / "config/research.yaml")
    papers, documents = _fixture()
    now = datetime(2026, 8, 29, tzinfo=UTC)
    first = rank_papers(
        papers,
        profile=config.research_profile,
        config=config.ranking,
        documents=documents,
        now=now,
    )
    second = rank_papers(
        papers,
        profile=config.research_profile,
        config=config.ranking,
        documents=documents,
        now=now,
    )
    assert [item.paper.identity for item in first] == [item.paper.identity for item in second]
    assert all(item.score.matched_terms for item in first)
    assert all(0 <= item.score.base_score <= 1 for item in first)


def test_no_zotero_redistributes_unavailable_weight():
    from auto_research_daily.ranking import score_paper

    config = load_config(ROOT / "config/research.yaml")
    papers, _ = _fixture()
    score = score_paper(
        papers[0],
        profile=config.research_profile,
        ranking=config.ranking,
        documents=(),
        now=datetime(2026, 8, 29, tzinfo=UTC),
    )
    r = config.ranking
    expected = (
        r.topic_weight * score.topic
        + r.recency_weight * score.recency
        + r.exploration_weight * score.exploration
    ) / (1 - r.personal_weight)
    assert abs(score.base_score - expected) < 1e-10


def test_generic_neural_papers_do_not_fill_empty_daily_pool():
    config = load_config(ROOT / "config/research.yaml")
    papers, _ = _fixture()
    unrelated = papers[0].model_copy(
        update={
            "title": "Neural Networks for Image Recognition",
            "abstract": "A transformer improves image classification with reinforcement learning.",
        }
    )
    assert rank_papers([unrelated], profile=config.research_profile, config=config.ranking) == []
