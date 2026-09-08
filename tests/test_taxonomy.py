from types import SimpleNamespace

import pytest

from auto_research_daily.taxonomy import classify_paper, classify_tags


def paper_item(
    *,
    title: str,
    abstract: str,
    primary_topic: str,
    tags: tuple[str, ...] = (),
    matched_terms: tuple[str, ...] = (),
) -> SimpleNamespace:
    return SimpleNamespace(
        analysis=SimpleNamespace(primary_topic=primary_topic, tags=tags),
        ranked=SimpleNamespace(
            paper=SimpleNamespace(title=title, abstract=abstract),
            score=SimpleNamespace(matched_terms=matched_terms),
        ),
    )


@pytest.mark.parametrize(
    ("expected", "title", "abstract", "topic"),
    [
        (
            "scheduling",
            "Flexible Job Shop Scheduling",
            "We assign operations to machines.",
            "生产调度",
        ),
        (
            "neural-optimization",
            "Neural Combinatorial Optimization",
            "We learn a graph neural solver.",
            "神经组合优化",
        ),
        (
            "agents-ai4or",
            "Large Language Model Agents for Automatic MILP",
            "A solver checks feasibility.",
            "自动建模",
        ),
        (
            "evolutionary-optimization",
            "Constrained Multi-Objective Evolutionary Optimization",
            "We use differential evolution.",
            "进化优化",
        ),
        ("frontier", "A New Decision Representation", "We study discrete choices.", "相邻方法"),
    ],
)
def test_classify_paper_uses_optimization_topics(expected, title, abstract, topic):
    assert (
        classify_paper(paper_item(title=title, abstract=abstract, primary_topic=topic)).key
        == expected
    )


def test_classify_tags_preserves_problem_and_method_axes():
    item = paper_item(
        title="Graph Neural Reinforcement Learning for Flexible Job Shop Scheduling",
        abstract="We study energy-efficient production scheduling.",
        primary_topic="生产调度",
        tags=("图神经网络", "强化学习"),
    )
    keys = {tag.key for tag in classify_tags(item)}
    assert {"job-shop", "graph-neural", "reinforcement-learning", "energy"} <= keys
