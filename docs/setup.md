# 服务配置

仓库 Settings → Secrets and variables → Actions。

| Secret | 用途 |
|---|---|
| LLM_API_KEY | DeepSeek 模型密钥 |
| SMTP_AUTH_CODE | 发件邮箱 SMTP 授权码 |
| SMTP_USERNAME | 发件邮箱完整地址 |
| MAIL_FROM | 发件地址 |
| MAIL_TO | 收件地址 |

| Variable | 值 |
|---|---|
| LLM_BASE_URL | https://api.deepseek.com |
| LLM_BRIEF_MODEL | deepseek-v4-flash |
| LLM_DEEP_MODEL | deepseek-v4-flash |
| SITE_URL | https://JiaqiTan111.github.io/Daily_Opt_Paper/ |
| SMTP_HOST | smtp.qq.com |
| SMTP_PORT | 465 |

Pages 发布来源选择 GitHub Actions。工作流自行申请仓库写入与 Pages 发布权限，无需另建个人访问令牌。首次手动触发可先用少量论文，并在希望发送邮件时勾选 send_email。

Zotero 当前关闭。以后接入时，在 https://www.zotero.org/settings/keys 创建仅允许读取个人库的密钥，将其保存为 ZOTERO_API_KEY，将用户数字 ID 保存为 ZOTERO_USER_ID，然后在 config/research.yaml 启用 zotero 并选择收藏夹。云端任务读取已同步的个人库，不直接连接本机 Zotero。

密钥和邮箱地址不写入公开源代码或运行数据。模型配置依据：https://api-docs.deepseek.com/ 。
