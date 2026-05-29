---
name: thesis-failure-mode-tree
description: PROVISIONAL Charter — 任何 thesis / hypothesis / investment doc MUST 含「5 大 failure mode 樹」，預先窮舉這個 thesis 可能怎麼死 + 對應監控指標 + 觸發 action
metadata:
  type: feedback
  scope: domain
  status: PROVISIONAL
  shadow_expiry: 2024-XX-XX
  pdpc_layer: signal
  upgrade_threshold:
    cases: 4
    correct_rate: 0.75
  downgrade_triggers:
    - 採信率 < 0.50
---

# Thesis Failure Mode 樹 (PDPC Domain SOP)

每份 thesis / hypothesis / investment doc MUST 含「**5 大 failure mode 樹**」— 預先窮舉這個 thesis 可能怎麼死。延伸 kill_switch 從**單一觸發**擴成**樹狀預演**。

## Why

只列「kill_switch」（這個 trigger 觸發就出場）通常**漏掉**：
- 死的方式有幾種（earnings / 競爭 / dilution / regime / disconfirming evidence）
- 每種對應監控指標
- 每種觸發 action

**真實案例**（投資 thesis 普遍踩雷）：thesis base data stale 30 天沒抓，因為 kill_switch 只盯 price + earnings event，沒盯 SEC filings / FCF 三源驗 / 稀釋風險。**failure mode 漏列**。

PDPC 解法：thesis MUST 含 5 mode 樹（不必每條都有 trigger，但 MUST 列出來做監控）。

## 5 大 Failure Mode（強制最低集合）

每個 thesis 至少回答這 5 mode 怎麼處理：

| # | Failure Mode | 監控指標 | 觸發 action |
|---|---|---|---|
| **1** | **Earnings miss / guidance cut** | 季度 EPS / Revenue / guidance 對比 consensus | miss > 5% → 重審 thesis pillar |
| **2** | **競爭結構崩壞** | 新進入者 / 替代品 / 客戶集中度 | 主客戶流失 > 20% → SUSPENDED |
| **3** | **Balance sheet 惡化 / 稀釋** | 可轉債發行 / 股權激勵比例 / 現金消耗 | 可轉債 > 20% 市值 → 重審稀釋 |
| **4** | **產業 / Macro regime 切換** | 大盤狀態 / 利率環境 / 監管變化 | Regime 切換 + > 50% drawdown → trim |
| **5** | **Thesis 本身錯（disconfirming evidence）** | 跨家紅隊驗證 / cross-vendor 對立 | 累積 ≥ 3 disconfirming → SUSPENDED 重寫 |

## thesis frontmatter 範本

```yaml
# 既有 frontmatter
kill_switch:
  - trigger: price < $X
    action: trim 50%
    status: ACTIVE

# 新增 failure_mode_tree
failure_mode_tree:
  earnings:
    monitor: EPS vs consensus quarterly
    threshold: miss > 5% OR guidance cut
    action: pillar re-review within 48h
    status: ACTIVE  # or NA(why)

  competitive:
    monitor: customer concentration / new entrants
    threshold: top-1 customer > 30% revenue
    action: thesis SUSPENDED until resolved
    status: ACTIVE

  dilution:
    monitor: convertible bond + SBC quarterly
    threshold: convertible > 20% market cap
    action: re-model EV per share
    status: ACTIVE

  macro_regime:
    monitor: regime transitions
    threshold: regime → Bear AND stock < -50% high
    action: trim to neutral
    status: ACTIVE

  thesis_disconfirming:
    monitor: cross-vendor 紅隊 / new evidence
    threshold: ≥ 3 disconfirming cases
    action: SUSPENDED + rewrite
    status: ACTIVE
```

**status 允許 `NA(理由)`** — 某 mode 不適用此 thesis 要明寫為什麼（如 SaaS 公司 dilution 不適用因為 zero debt）。

## How to apply

### 新 thesis 寫作 SOP

寫新 thesis MUST 跑：

1. 寫 thesis 主文 + kill_switch（既有 falsifiable 流程）
2. **新增**：寫 failure_mode_tree 5 mode（每個 ACTIVE 或 NA(why)）
3. **新增**：grep 既有 thesis 看是否已有同類 mode → 累積案例
4. Operator ack 後存檔

### 既有 thesis 補做

不強制 backfill 全部（避免過度擴張），但**大改 thesis 時 MUST 補 failure_mode_tree**。

### 監控 cron

寫 `thesis_failure_mode_monitor.py` daily 跑：
- grep `theses/*/thesis.md` 抓 failure_mode_tree
- 對每個 mode 用 data source（SEC / API / cross-vendor 紅隊 log）檢查 threshold
- 任一 mode threshold 觸發 → inbox alert

## PDPC 哲學

「最適策追究」紀律的 **domain SOP 層**應用：對 thesis 死法窮舉所有可能 → 對應監控 + action。

跟 [signal-event-reaction-tree](04-signal-event-reaction-tree.md) 不同：
- signal event 是**高頻反應**（每月數次）
- thesis failure mode 是**低頻預警**（每季一次 review）

兩者互補：signal 樹處理「當下事件」，failure mode 樹處理「結構性死法」。

## SHADOW → CONFIRMED 條件

（依 meta charter Domain SOP 格）

- 60 天內套用 ≥ 4 個 thesis
- 採信率 ≥ 75%（70% 案例的 mode 預先抓到後續真實 failure）
- Operator 沒抱怨

## 連結

- 哲學源頭：PDPC 最適策追究（domain SOP 層）
- 配套：[signal-event-reaction-tree](04-signal-event-reaction-tree.md) — 高頻反應姊妹
- 配套：[regime-switch-pdpc](05-regime-switch-pdpc.md) — macro mode 之一細化
- Meta：[promotion-demotion-meta](01-promotion-demotion-meta.md)
