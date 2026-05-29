---
name: signal-event-reaction-tree
description: PROVISIONAL Charter — 高頻 signal event (e.g., earnings call / FOMC / 公司公告) 反應 MUST 走預先窮舉的 PDPC 樹，不靠當下臨場判
metadata:
  type: feedback
  scope: signal
  status: PROVISIONAL
  shadow_expiry: 2024-XX-XX
  pdpc_layer: signal
  upgrade_threshold:
    cases: 4
    correct_rate: 0.75
  downgrade_triggers:
    - Operator 抱怨「太機械化」
---

# Signal Event Reaction PDPC（最高頻決策層）

每個高頻 signal event 後 MUST 走預先窮舉的 PDPC 樹，**不靠當下臨場判**。

## Why

高頻 signal events（earnings call / Fed meeting / 公司公告 / breakout 訊號）是 agent 最容易亂的場景：
- Miss → operator 容易 panic sell
- Beat → 容易過度 chase (FOMO)
- 同樣 input，不同 session 給不同建議 — **一致性差**

PDPC 解法：**預先窮舉**「signal × context × position state」維度 → 對應決策樹。

## Example: Earnings Call Reaction (3×3 PDPC)

以 earnings call 為例（其他 signal event 同理可套）：

3 維 = EPS surprise × Guidance × Position state

|  | Guidance Raise | Guidance Hold | Guidance Cut |
|---|---|---|---|
| **EPS Beat** | **A1**：thesis 強化 → hold / 加碼觀察 | **A2**：beat 但管理層保守 → hold / 留意 | **A3**：beat 但 cut guide = **預警** → 重審 thesis pillar |
| **EPS Inline** | **B1**：guide raise = forward leaning → hold | **B2**：純 inline → hold（無動作）| **B3**：cut guide = warning → trim 1/3 |
| **EPS Miss** | **C1**：miss 但 raise = 一次性 → 看細節 | **C2**：miss + hold = 真實放緩 → trim 1/3 | **C3**：miss + cut = 雙降 → **kill switch 觸發** |

**動作梯度**：
- hold = 不動
- 加碼觀察 = 加 0.5×（半倉位試水溫）
- 重審 thesis pillar = 48h 內跑 5 mode failure 檢查
- trim 1/3 = 砍 33% 持倉降風險
- kill switch 觸發 = 走 thesis 預設 exit action

## Position State Modifier (×2 細分)

每個情境再分 position state：

| Position 類別 | modifier |
|---|---|
| **Core position** (≥ 5% portfolio) | 走表，但「重審」改 72h、「trim」改保守版（1/3 不 1/2）|
| **Watchlist position** (< 2% portfolio) | 走表，但「重審」改 24h、「trim」改激進版（1/2 不 1/3）|
| **New position** (< 3 months held) | **任何 miss 都 kill switch 觸發**（沒驗證 thesis 還不該抱負面）|

## Reaction Time PDPC

| Event 出來後 | 動作 |
|---|---|
| **0-15 min** | 看數字 + opening 5 min → 對照矩陣 → 標記情境 |
| **15-30 min** | grep thesis + 跑 failure mode 樹比對 → 判斷情境 modifier |
| **30 min 內** | 寫 inbox alert：「{asset} event 落 {情境代碼} → 建議 {動作} → 等 operator 決定」|
| **next session open 30 min 前** | 看 pre-market price → 對照預設動作 → 下單或 hold |

**禁**：30 min 內就下單（給 operator 決定空間，agent 不代決）。

## How to apply

### Event 季前準備（提前 1 週）

1. grep asset thesis 看 kill_switch + failure_mode
2. 標記 PDPC 矩陣中「會觸發 kill switch」的格子（通常 C2 / C3）
3. 預寫 pre-mortem：「如果落 C3 我會做什麼」

### Event 當天

Agent 自動觸發 SOP（不需要 operator 問）：
1. 抓 actual + consensus → 對照差異
2. 找 PDPC 矩陣對應格
3. 加 position state modifier
4. 報告：「{asset} 落 {代碼+modifier} → 預設動作 {X} → operator 30 min 內回應 or 走預設」

### Ledger 紀錄

寫到 `events_log.jsonl`：

```json
{
  "date": "2024-XX-XX",
  "asset": "XXX",
  "event_type": "earnings_call",
  "case": "B2",
  "modifier": "core",
  "pre_action": "hold",
  "post_30d_return": "+5.2%",
  "thesis_outcome": "correct"
}
```

季度 review 跑 PDPC 採信率算（meta charter 升級閘門用）。

## 例外狀況

- **大 beat (> 20%) + 大漲 (> 15% AH)** → 不在矩陣 → 走 FOMO 紅旗 stop（避免加碼錯）
- **First event after onboarding**（如 IPO 後第一次）→ 任何 miss 都 kill switch 觸發
- **Management 異動同期** → 矩陣跳過，走 thesis SUSPENDED 重審路徑

## PDPC 哲學

「最適策追究」紀律的**signal 層**應用：預先窮舉所有 signal × context combo → 對應動作樹。

「signal event 反應」是 agent 最高頻決策（每月數次 - 數十次觸發）+ 最容易混亂的場景。把臨場判斷外部化成樹是核心紀律。

## SHADOW → CONFIRMED 條件

（依 meta charter Domain SOP 格）

- 60 天內套用 ≥ 4 次 events
- 採信率 ≥ 75%（情境判斷對 + 動作後 30 天回望結果正確）
- Operator 沒抱怨「太機械化」

## 連結

- 哲學源頭：PDPC 最適策追究（signal 層 / 最高頻應用）
- 配套：[thesis-failure-mode-tree](07-thesis-failure-mode-tree.md) — failure mode 5-tree 細化
- 配套：[regime-switch-pdpc](05-regime-switch-pdpc.md) — macro 層姊妹
- Meta：[promotion-demotion-meta](01-promotion-demotion-meta.md)
