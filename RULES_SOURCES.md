# 规则来源说明

本仓库提供以下规则：

- **all**：Siri 2 + Siri 3 + Meta Muse + Telegram 推送（推荐）
- **muse**：仅 Meta Muse
- **siri2**：仅二代 Siri / Apple Intelligence
- **siri3**：仅三代 Siri（含二代域名 + iOS 27 新增接入点）
- **telegram**：仅 Telegram 推送（APNs）

所有完整 `.conf` 文件均基于 [Johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever) 的 `sr_top500_whitelist_ad.conf` 叠加生成，每日自动更新。

---

## Meta Muse（lists/muse.list / all.list 中的 Muse 部分）

主要来源：

1. **[juner922/muse-loon-rules](https://github.com/juner922/muse-loon-rules)** 的 `MuseAI.list`
   - 基于 Meta Muse 客户端二进制逆向分析（[mahdi-salmanzade/meta-muse-teardown](https://github.com/mahdi-salmanzade/meta-muse-teardown)）
   - 经 NodeSeek、Linux.do、V2EX 等社区用户实测日志交叉核实
   - 覆盖 Muse 专用域名（`muse.ai`、`metaaivm.com`、`ecto1usercontent.com`、Hatch/Secure VM 相关等）以及 Meta 账号与社交基础设施（Facebook / Instagram / WhatsApp）

2. **[VPSDance/ai-proxy-rules](https://github.com/VPSDance/ai-proxy-rules)** 的 `meta-ai.list`
   - 补充通用 Meta AI / Llama 相关域名（`ai.meta.com`、`llama.com`、`llamameta.net`、`atmeta.com` 等）
   - 与 juner922 列表互补：后者更侧重 Muse 专用后端，前者覆盖更广泛的 Meta AI 产品

社区实测最小可用集通常为：`muse.ai` + `meta.com` + `metaaivm.com`。  
地区限制主要看出口 IP，建议使用美国或新加坡住宅节点，机房 IP 容易被等待名单。

---

## 二代 Siri（lists/siri2.list）

Apple Intelligence + ChatGPT 扩展 / Private Cloud Compute 相关域名。

核心域名包括：
- `guzzoni.apple.com`（Siri / 听写主网关）
- `smoot.apple.com`（Siri / Spotlight / Lookup 搜索）
- `apple-relay.*`（Private Cloud Compute / Private Relay 中继，含 Cloudflare、Fastly 等）
- `mask.icloud.com` / `mask-api.icloud.com` / `mask-*.apple-dns.net` 等
- `gspe1-ssl.ls.apple.com`（定位服务）
- `cp4.cloudflare.com`
- `apple-intelligence` 关键字

**主要来源**：

1. **Apple 官方文档** [Use Apple Intelligence with Siri](https://support.apple.com/en-us/101555)  
   官方提及的相关域名与 Private Cloud Compute / Private Relay 说明。

2. **社区规则仓库**：
   - [ma-wenqian/ai-proxy-rules](https://github.com/ma-wenqian/ai-proxy-rules) 的 `rules/apple-intelligence.list`（较完整的 Apple Intelligence / Siri / Private Relay 集合）
   - [iab0x00/ProxyRules](https://github.com/iab0x00/ProxyRules) 的 `Rule/AppleIntelligence.txt`（简洁实用版，含 wildcard）
   - [LingJingMaster/Shadowrocket-Rules](https://github.com/LingJingMaster/Shadowrocket-Rules) 的 `AI.list`（Apple Intelligence 部分）
   - [Accademia/Additional_Rule_For_Clash](https://github.com/Accademia/Additional_Rule_For_Clash) 的 `AppleAI/AppleAI_Domain.yaml`（基于官方文档整理）
   - [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) PR #1628（AppleIntelligence 规则，参考官方文档）

3. **Johnshall 仓库用户反馈**：  
   [Issue #565](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever/issues/565) 中用户提交的最小可用集（`guzzoni` + `apple-relay.*` + `smoot` + `gspe1-ssl.ls.apple.com` + `cp4.cloudflare.com`）。

4. 其他社区实测与 v2fly / MetaCubeX 等规则集的补充讨论。

早期 Apple Intelligence / Siri 2 社区实测规则整理，持续维护在本仓库。

---

## 三代 Siri（lists/siri3.list）

在二代基础上增加 iOS 27 Siri AI 云端接入点，例如：
- `seed.siri.apple.com` / `seed-sequoia.siri.apple.com` / `seed-swallow.siri.apple.com`
- `api-siri-prod.apple.com`
- `mask-api.fe2.apple-dns.net`
- `apple-carry-relay.cloudflare.com` / `apple-relay.akamaized.net`
- `probe.icloud.com` / `metrics.icloud.com`
- `siri.apple.com` / `siri.com` 后缀

**主要来源**：

1. **iOS 27 Siri AI 社区实测与抓包**：  
   - [V2EX 帖子：非国行 iPhone 开启 iOS27 new siri 规则分享](https://www.v2ex.com/t/1241284)（含 `seed.siri.apple.com`、`probe.icloud.com`、`metrics.icloud.com`、`api-siri-prod.apple.com` 等）
   - [Hawaiine/mihomo-rules](https://github.com/Hawaiine/mihomo-rules) 的 `ruleset/SiriAI/SiriAI.yaml`
   - 其他社区 Issue 与用户反馈（如 Kianuni 相关仓库讨论）

2. **新增接入点整理**：  
   在二代核心域名基础上，根据 iOS 27 系统抓包与社区实测持续追加的云端域名（seed 系列、api-siri-prod、apple-carry-relay 等）。

3. 参考 [BrownieCoder/SiriAI-RouteKit](https://github.com/BrownieCoder/SiriAI-RouteKit) 等针对 Siri AI 的专门规则项目。

---

## Telegram 推送（lists/telegram.list）

解决 iPhone 锁屏收不到 Telegram 通知的问题，通过让 Apple 推送服务（APNs）相关域名和 IP 走代理实现。

包含：
- `push.apple.com` 及相关域名
- Apple 推送服务常用 IP 段（`17.249.0.0/16`、`17.252.0.0/16`、`17.57.144.0/22`、`17.188.128.0/18` 等，含 IPv6）

**来源**：
- 社区实测方案（主要来自 X / 小火箭用户分享）
- 与常见 APNs 代理修复方案一致

**使用注意（2026-11-17 实测更新）**：
- 仅添加规则即可正常收到 Telegram 推送，**无需**开启「包括所有网络」和「包括 APNs」。
- 开启「包括所有网络」会导致 Apple Watch 网络连接异常（手表无法连网）。
- 建议保持这两个开关关闭，以兼顾 Telegram 推送和手表正常使用。

---

## 整合规则（lists/all.list）

直接合并 siri2.list + siri3.list 中的差异部分 + muse.list 全部内容 + telegram.list，一次导入即可覆盖全部。

---

## 维护说明

- 规则源文件（`lists/*.list`）手工维护
- `scripts/patch_johnshall.py` 每日从 Johnshall 拉取最新基础配置并叠加各 `*.list`，输出到 `configs/`
- GitHub Actions 自动生成并提交完整 `.conf` 文件

如有新域名需要补充，欢迎提 Issue 或 PR。
