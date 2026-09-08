# PaperDaily

面向智能优化、生产调度与人工智能驱动运筹优化的个人每日论文工具。

[阅读网站](https://JiaqiTan111.github.io/Daily_Opt_Paper/) · [每日工作流](https://github.com/JiaqiTan111/Daily_Opt_Paper/actions/workflows/daily.yml) · [研究画像依据](docs/research-profile.md) · [配置说明](docs/setup.md) · [项目来源](UPSTREAM.md)

系统从 arXiv 获取近期论文，先按优化问题与方法筛选，再生成有证据约束的中文解读，输出日报、历史论文库、主题和标签档案、RSS 与邮件。优先关注神经网络、强化学习和智能体如何参与建模与求解。

每天北京时间 08:00 主触发，10:17 和 13:43 检查并恢复未完成的投递。GitHub Actions 可能排队，08:00 是触发时间，非保证送达时间。每次回溯 3 天，最多分析 60 篇、发布 40 篇、读取正文节选 10 篇。质量不足时不补足数量。

模型为 DeepSeek `deepseek-v4-flash`，摘要与正文均使用非思考模式。摘要输出上限 2500、正文输出上限 5000 令牌，并发 4。沿用参考仓库的数量与缓存预算，不设未经用户指定的金额硬上限。

第一版暂不接入 Zotero。排序自动重新分配不可用的个人语料权重；通用神经网络或智能体论文须明确涉及优化问题才进入模型分析。研究画像由用户指定方向与公开代表工作校准，并非作者追踪订阅。目前数据源是 arXiv，未覆盖仅在期刊出版的全部论文。

## 本地验证

```bash
uv sync --frozen --extra dev
uv run auto-research-daily validate
uv run ruff check src tests
uv run pytest
uv run auto-research-daily daily --offline-fixture tests/fixtures/offline_daily.json --no-llm --dry-run
```

离线样例是明确标识的合成测试数据，不可作为真实论文发布。正式运行需要 `LLM_API_KEY`；设置 `SITE_URL` 后执行 `uv run auto-research-daily daily`。`--dry-run` 仅禁止写入，若未同时使用离线样例与 `--no-llm`，仍可能发生接口调用与计费。

## 输出与证据

`reports/` 保存中文日报，`data/daily/` 保存每次日报，`data/archive/` 合并月度记录，`site/` 部署网页。正文来自 arXiv HTML 分层节选，获取失败退回摘要；不将摘要级解读当作全文结论。原图只增强阅读，不参与模型分析。通知状态防止同日重复发信和跨日重复推荐同一论文版本。
