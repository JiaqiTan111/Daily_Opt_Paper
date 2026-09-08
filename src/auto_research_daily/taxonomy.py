from __future__ import annotations

import unicodedata
from dataclasses import dataclass

from auto_research_daily.models import AnalyzedPaper


@dataclass(frozen=True, slots=True)
class ResearchTopic:
    key: str
    label: str
    description: str
    terms: tuple[str, ...]
    abstract_weight: int = 1


@dataclass(frozen=True, slots=True)
class ResearchTag:
    key: str
    label: str
    description: str
    aliases: tuple[str, ...]


RESEARCH_TOPICS: tuple[ResearchTopic, ...] = (
    ResearchTopic(
        "scheduling",
        "生产调度",
        "车间、流水线、装配与生产运输协同的调度建模和求解。",
        (
            "job shop",
            "job-shop",
            "flow shop",
            "flowshop",
            "flow-shop",
            "production scheduling",
            "manufacturing scheduling",
            "车间",
            "生产调度",
            "流水",
            "装配调度",
        ),
    ),
    ResearchTopic(
        "evolutionary-optimization",
        "进化与智能优化",
        "进化计算、群智能、约束多目标、多任务与昂贵优化。",
        (
            "evolutionary",
            "differential evolution",
            "swarm",
            "memetic",
            "multiobjective",
            "multi-objective",
            "many-objective",
            "进化",
            "群智能",
            "多目标",
            "差分进化",
        ),
    ),
    ResearchTopic(
        "neural-optimization",
        "神经组合优化",
        "图表示、神经求解器、生成式优化与学习辅助搜索。",
        (
            "neural combinatorial",
            "neural solver",
            "graph neural",
            "pointer network",
            "learning to optimize",
            "learning to search",
            "神经组合",
            "图神经",
            "神经求解",
        ),
    ),
    ResearchTopic(
        "reinforcement-learning",
        "强化学习求解",
        "构造式策略、局部改进、调度规则和求解器策略学习。",
        (
            "reinforcement learning",
            "deep q-network",
            "q-learning",
            "policy optimization",
            "强化学习",
            "策略优化",
        ),
    ),
    ResearchTopic(
        "agents-ai4or",
        "智能体与自动建模",
        "多智能体协同、大模型启发式生成、运筹建模与工具调用。",
        (
            "multi-agent",
            "multiagent",
            "agentic",
            "large language model",
            "automatic milp",
            "自动建模",
            "大模型",
            "智能体",
        ),
    ),
    ResearchTopic(
        "mathematical-programming",
        "数学规划与混合求解",
        "整数规划、约束规划、分解、界与学习辅助精确求解。",
        (
            "mixed integer",
            "mixed-integer",
            "integer programming",
            "constraint programming",
            "branch-and-bound",
            "branch and bound",
            "整数规划",
            "约束规划",
            "数学规划",
        ),
    ),
    ResearchTopic(
        "routing-resources",
        "路径与资源优化",
        "路径规划、车辆路径、项目调度与资源配置。",
        (
            "vehicle routing",
            "traveling salesman",
            "travelling salesman",
            "resource allocation",
            "project scheduling",
            "车辆路径",
            "资源分配",
            "项目调度",
        ),
    ),
    ResearchTopic(
        "benchmark",
        "基准与复现",
        "测试实例、公平比较、泛化和可复现评测。",
        (
            "benchmark suite",
            "benchmarking platform",
            "evaluation framework",
            "评测基准",
            "基准平台",
        ),
    ),
    ResearchTopic("frontier", "前沿探索", "与研究主线有明确联系的相邻方法与问题。", ()),
)

TOPIC_BY_KEY = {topic.key: topic for topic in RESEARCH_TOPICS}

RESEARCH_TAGS: tuple[ResearchTag, ...] = (
    ResearchTag("job-shop", "作业车间", "作业车间", ("job shop", "job-shop", "作业车间")),
    ResearchTag(
        "flow-shop", "流水车间", "流水车间", ("flow shop", "flowshop", "flow-shop", "流水车间")
    ),
    ResearchTag(
        "distributed",
        "分布式制造",
        "分布式制造",
        (
            "distributed scheduling",
            "distributed manufacturing",
            "distributed flow",
            "distributed heterogeneous",
            "分布式",
        ),
    ),
    ResearchTag(
        "dynamic-robust",
        "动态与鲁棒",
        "动态与鲁棒",
        (
            "dynamic scheduling",
            "machine breakdown",
            "uncertainty",
            "robust optimization",
            "动态",
            "鲁棒",
            "不确定",
        ),
    ),
    ResearchTag(
        "energy",
        "能效与绿色制造",
        "能效与绿色制造",
        ("energy-efficient", "energy-aware", "energy efficient", "能效", "能耗", "绿色制造"),
    ),
    ResearchTag(
        "multi-objective",
        "约束多目标",
        "约束多目标",
        ("multi-objective", "multiobjective", "many-objective", "多目标", "约束优化"),
    ),
    ResearchTag(
        "reinforcement-learning",
        "强化学习",
        "强化学习",
        ("reinforcement learning", "q-learning", "deep q-network", "强化学习"),
    ),
    ResearchTag("graph-neural", "图神经网络", "图神经网络", ("graph neural", "图神经")),
    ResearchTag(
        "agents", "多智能体", "多智能体", ("multi-agent", "multiagent", "agentic", "智能体")
    ),
    ResearchTag(
        "llm", "大模型辅助优化", "大模型辅助优化", ("large language model", "大模型", "自动建模")
    ),
    ResearchTag(
        "evolutionary",
        "进化与群智能",
        "进化与群智能",
        ("evolutionary", "differential evolution", "memetic", "swarm", "进化", "群智能"),
    ),
    ResearchTag(
        "mathematical-programming",
        "数学规划",
        "数学规划",
        (
            "integer programming",
            "mixed-integer",
            "mixed integer",
            "constraint programming",
            "整数规划",
            "约束规划",
        ),
    ),
    ResearchTag(
        "transfer-surrogate",
        "迁移与代理模型",
        "迁移与代理模型",
        (
            "knowledge transfer",
            "transfer learning",
            "surrogate",
            "multitask",
            "迁移",
            "代理模型",
            "多任务",
        ),
    ),
    ResearchTag(
        "benchmark",
        "基准与泛化",
        "基准与泛化",
        ("benchmark", "generalization", "reproducibility", "基准", "泛化", "复现"),
    ),
)

TAG_BY_KEY = {tag.key: tag for tag in RESEARCH_TAGS}


def _normalize(value: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def classify_paper(item: AnalyzedPaper) -> ResearchTopic:
    """Project a fine-grained analysis onto one stable public research shelf."""

    analysis = item.analysis
    paper = item.ranked.paper
    title = _normalize(paper.title)
    metadata = _normalize(
        " ".join(
            (
                analysis.primary_topic,
                *analysis.tags,
                *item.ranked.score.matched_terms,
            )
        )
    )
    abstract = _normalize(paper.abstract)

    scored: list[tuple[int, int, ResearchTopic]] = []
    for priority, topic in enumerate(RESEARCH_TOPICS[:-1]):
        score = 0
        for raw_term in topic.terms:
            term = _normalize(raw_term)
            if term in title:
                score += 5
            if term in metadata:
                score += 4
            if term in abstract:
                score += topic.abstract_weight
        scored.append((score, -priority, topic))

    best_score, _, best_topic = max(scored, key=lambda entry: (entry[0], entry[1]))
    return best_topic if best_score else TOPIC_BY_KEY["frontier"]


def classify_tags(item: AnalyzedPaper) -> tuple[ResearchTag, ...]:
    analysis = item.analysis
    paper = item.ranked.paper
    signal = _normalize(
        " ".join(
            (
                analysis.primary_topic,
                *analysis.tags,
                *item.ranked.score.matched_terms,
                paper.title,
                paper.abstract,
            )
        )
    )
    return tuple(
        tag for tag in RESEARCH_TAGS if any(_normalize(alias) in signal for alias in tag.aliases)
    )


def paper_search_text(item: AnalyzedPaper, topic: ResearchTopic) -> str:
    analysis = item.analysis
    paper = item.ranked.paper
    return _normalize(
        " ".join(
            (
                topic.label,
                analysis.primary_topic,
                *analysis.tags,
                paper.title,
                analysis.title_zh,
                *paper.authors,
                paper.abstract,
                analysis.setting,
                analysis.motivation,
                analysis.insight,
                analysis.analysis,
                *analysis.method,
                *analysis.experiments,
                analysis.relation_to_research,
                analysis.why_recommended,
            )
        )
    )
