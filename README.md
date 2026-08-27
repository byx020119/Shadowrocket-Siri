# Shadowrocket Siri / Muse / Telegram 推送规则

中国大陆网络下用 Shadowrocket 导出 Apple Intelligence / Siri / Meta Muse / Telegram 推送流量。
每天基于 [Johnshall](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever) 白名单+去广告重建完整配置。建议美国或新加坡住宅节点。

## 推荐：整合规则（一次导入全部）

覆盖：二代 Siri + 三代 Siri AI + Meta Muse + Telegram 推送

```
https://raw.githubusercontent.com/byx020119/Shadowrocket-Siri/main/configs/sr_top500_whitelist_ad_all.conf
```

<p align="center">
  <img src="https://api.qrserver.com/v1/create-qr-code/?size=280x280&margin=12&data=https%3A%2F%2Fraw.githubusercontent.com%2Fbyx020119%2FShadowrocket-Siri%2Fmain%2Fconfigs%2Fsr_top500_whitelist_ad_all.conf" width="280" alt="All QR" />
</p>

小火箭：配置 → **+→ 从 URL 下载** → 粘贴或扫码 → **使用配置**。

### Telegram 推送使用说明

使用本规则后，Telegram 推送可正常工作。

**实测结论（2026-11-17）**：
- **无需**开启「包括所有网络」和「包括 APNs」即可正常收到推送。
- 开启「包括所有网络」会导致 Apple Watch 网络连接异常。
- 建议保持这两个开关关闭。

---

## 单独规则（按需使用）

<details>
<summary>点击展开查看各单项规则链接和二维码</summary>

### Meta Muse

```
https://raw.githubusercontent.com/byx020119/Shadowrocket-Siri/main/configs/sr_top500_whitelist_ad_muse.conf
```

<p align="center">
  <img src="https://api.qrserver.com/v1/create-qr-code/?size=220x220&margin=10&data=https%3A%2F%2Fraw.githubusercontent.com%2Fbyx020119%2FShadowrocket-Siri%2Fmain%2Fconfigs%2Fsr_top500_whitelist_ad_muse.conf" width="220" alt="Muse QR" />
</p>

### 二代 Siri

```
https://raw.githubusercontent.com/byx020119/Shadowrocket-Siri/main/configs/sr_top500_whitelist_ad_siri2.conf
```

<p align="center">
  <img src="https://api.qrserver.com/v1/create-qr-code/?size=220x220&margin=10&data=https%3A%2F%2Fraw.githubusercontent.com%2Fbyx020119%2FShadowrocket-Siri%2Fmain%2Fconfigs%2Fsr_top500_whitelist_ad_siri2.conf" width="220" alt="Siri 2 QR" />
</p>

### 三代 Siri（iOS 27 Siri AI）

```
https://raw.githubusercontent.com/byx020119/Shadowrocket-Siri/main/configs/sr_top500_whitelist_ad_siri3.conf
```

<p align="center">
  <img src="https://api.qrserver.com/v1/create-qr-code/?size=220x220&margin=10&data=https%3A%2F%2Fraw.githubusercontent.com%2Fbyx020119%2FShadowrocket-Siri%2Fmain%2Fconfigs%2Fsr_top500_whitelist_ad_siri3.conf" width="220" alt="Siri 3 QR" />
</p>

### Telegram 推送

```
https://raw.githubusercontent.com/byx020119/Shadowrocket-Siri/main/configs/sr_top500_whitelist_ad_telegram.conf
```

<p align="center">
  <img src="https://api.qrserver.com/v1/create-qr-code/?size=220x220&margin=10&data=https%3A%2F%2Fraw.githubusercontent.com%2Fbyx020119%2FShadowrocket-Siri%2Fmain%2Fconfigs%2Fsr_top500_whitelist_ad_telegram.conf" width="220" alt="Telegram QR" />
</p>

</details>

---

规则来源详细说明见 [`RULES_SOURCES.md`](https://github.com/byx020119/Shadowrocket-Siri/blob/main/RULES_SOURCES.md)。
