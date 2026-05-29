---
name: thesis-failure-mode-tree
description: PROVISIONAL Charter — Any thesis / hypothesis / investment doc MUST contain a "5 failure mode tree". Pre-enumerate all ways this thesis could die + monitoring indicators + triggered action.
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
    - correct_rate < 0.50
---

# Thesis Failure Mode Tree (PDPC Domain SOP)

Every thesis / hypothesis / investment doc MUST contain a "**5 failure mode tree**" — pre-enumerate all ways this thesis could die. Extends kill_switch from **single trigger** to **tree-structured pre-play**.

## Why

Only listing "kill_switch" (when this trigger fires, exit) typically **misses**:
- How many ways could it die (earnings / competitive / dilution / regime / disconfirming evidence)
- Monitoring indicators for each
- Triggered action for each

**Real case** (investment theses generally fall into this trap): thesis base data stale 30 days uncaught, because kill_switch only watches price + earnings event, doesn't watch SEC filings / FCF triangulation / dilution risk. **Failure modes incompletely listed**.

PDPC solution: thesis MUST contain 5-mode tree (each mode doesn't need a trigger, but MUST be listed for monitoring).

## 5 Failure Modes (minimum required set)

Each thesis must answer how to handle these 5 modes:

| # | Failure Mode | Monitoring Indicator | Triggered Action |
|---|---|---|---|
| **1** | **Earnings miss / guidance cut** | Quarterly EPS / Revenue / guidance vs consensus | miss > 5% → re-review thesis pillar |
| **2** | **Competitive structure collapse** | New entrants / substitutes / customer concentration | top-1 customer loss > 20% → SUSPENDED |
| **3** | **Balance sheet deterioration / dilution** | Convertible issuance / SBC ratio / cash burn rate | convertible > 20% market cap → re-model dilution |
| **4** | **Industry / Macro regime switch** | Market state / interest rate / regulation | Regime → Bear AND stock < -50% high → trim |
| **5** | **Thesis itself wrong (disconfirming evidence)** | Cross-vendor red team / new evidence | ≥ 3 disconfirming cases → SUSPENDED rewrite |

## Thesis Frontmatter Template

```yaml
# existing frontmatter
kill_switch:
  - trigger: price < $X
    action: trim 50%
    status: ACTIVE

# new: failure_mode_tree
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

**status allows `NA(reason)`** — if a mode doesn't apply to this thesis, explicitly state why (e.g., SaaS company with zero debt → dilution NA).

## How to Apply

### New Thesis Writing SOP

When writing new thesis MUST run:

1. Write thesis main text + kill_switch (existing falsifiable flow)
2. **New**: write failure_mode_tree 5 modes (each ACTIVE or NA(why))
3. **New**: grep existing theses for same-type mode → accumulate cases
4. Operator acks → save

### Backfilling Existing Theses

Don't force backfill on all (avoid scope creep), but **MUST add failure_mode_tree when significantly editing thesis**.

### Monitoring Cron

Write `thesis_failure_mode_monitor.py` daily:
- grep `theses/*/thesis.md` for failure_mode_tree
- For each mode, use data source (SEC / API / cross-vendor red team log) check threshold
- Any mode threshold triggered → inbox alert

## PDPC Philosophy

Application of "saitekisaku tsuikyu" at the **domain SOP layer**: exhaustive enumeration of how thesis can die → corresponding monitoring + action.

Differs from [signal-event-reaction-tree](04-signal-event-reaction-tree.md):
- Signal event is **high-frequency reaction** (several per month)
- Thesis failure mode is **low-frequency early warning** (quarterly review)

The two are complementary: signal tree handles "current events", failure mode tree handles "structural ways to die".

## SHADOW → CONFIRMED Conditions

(Per meta charter Domain SOP row)

- Within 60 days, applied to ≥ 4 theses
- Correct rate ≥ 75% (70% of cases' modes pre-captured actual future failure)
- Operator didn't complain

## Links

- Philosophical source: PDPC saitekisaku tsuikyu (domain SOP layer)
- Companion: [signal-event-reaction-tree](04-signal-event-reaction-tree.md) — high-frequency reaction sibling
- Companion: [regime-switch-pdpc](05-regime-switch-pdpc.md) — §macro mode 細化
- Meta: [promotion-demotion-meta](01-promotion-demotion-meta.md)

---
---

# 中文版本

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
