---
name: regime-switch-pdpc
description: PROVISIONAL Charter — Macro regime transitions must follow a pre-enumerated action tree, not in-the-moment improvisation.
metadata:
  type: feedback
  scope: macro
  status: PROVISIONAL
  shadow_expiry: 2024-XX-XX
  pdpc_layer: macro
  upgrade_threshold:
    cases: 4
    correct_rate: 0.75
  downgrade_triggers:
    - Operator complains "too mechanical"
---

# Macro Regime Switch PDPC

Macro regime transitions MUST follow a pre-enumerated action tree, not in-the-moment improvisation.

## Why

Macro regime transitions are **low-frequency, high-impact events** (2-4 major switches per year):
- Bull → Bear transition triggers easy panic
- Bear → Bull reverse causes missed opportunity
- Each time agent "re-thinks" countermeasures → same transition gives different recommendations in different sessions

PDPC solution: pre-enumerate "regime × switch direction × position class" → action.

## 5 Regime Buckets

Group by your macro framework (example uses 5 buckets, can be 13/24/N):

| Group | Description | Macro Meaning |
|---|---|---|
| **🟢 Bull Aligned** | Multi-asset uptrend | Clear bull |
| **🟡 Bull Recover** | Recovering from bear | Momentum turning positive |
| **⚪ Neutral** | Sideways / Choppy | No clear direction |
| **🟠 Bear Recover** | Bounce within bear | False rally risk |
| **🔴 Bear Aligned** | Multi-asset downtrend | Clear bear |

## 5×5 Switch Reaction PDPC Tree

```
From → To             | Strength | Position Action
─────────────────────┼─────────┼──────────────────────────────
🟢 Bull → 🟡 Recover  | weak    | observe, no action
🟢 Bull → ⚪ Neutral  | medium  | Core trim 10%, clear watchlist
🟢 Bull → 🟠 Bear Rec | strong  | Core trim 25%, clear watchlist
🟢 Bull → 🔴 Bear     | extreme | Core trim 50%, cash up to 30%+
🟡 Recover → 🟢 Bull  | scale-up | watchlist → core, add 5-10%
🟡 → 🔴 Bear          | reversal | Core trim 33%, cash up to 25%+
⚪ Neutral → 🟢 Bull   | scale-up | watchlist add 50%
⚪ Neutral → 🔴 Bear   | defensive | Core trim 15%, cash 20%+
🟠 Bear Rec → 🟢 Bull  | confirmed reversal | aggressive add, core back to 80%+
🟠 Bear Rec → 🔴 Bear  | false rally | trim defensively, cash 30%+
🔴 Bear → 🟠 Recover  | testing bottom | observe, 1/3 add watchlist
🔴 Bear → 🟡 Recover  | recovery | Core back from 40% to 60-70%
🔴 Bear → 🟢 Bull     | bull market resumed | full scale, cash down to 5-10%
```

**Micro-switches within same bucket** don't count as major switch, hold no action.

## Asset Modifier (×3 細分)

Regime switch doesn't need to treat every position uniformly. Look at asset state:

| Asset state | modifier |
|---|---|
| **Strong momentum + uptrend** | switch action **halved** (asset strong, hold longer) |
| **Weak momentum + downtrend** | switch action **doubled** (asset weak, trim faster) |
| **Middle state** | follow table |

## Switch Confirmation Rules (avoid whipsaw)

PDPC triggers only if:

1. Regime switch **confirmed for 5 consecutive trading days** (not a single-day jump)
2. Not in earnings season (avoid event interference)
3. Volatility index direction matches (Bull → Bear must have VIX rising)

If any condition fails → mark `pending confirm`, re-check in 14 days.

## How to Apply

### Daily Cron

`daily_regime_monitor.py`:
- Daily EOD captures current regime
- Compare to 5-day-ago regime
- If switched → run 3 confirmation rules
- All pass → inbox alert: "Regime switched from {A} to {B}, PDPC tree suggests: {action}"

### Agent Trigger

After regime switch alert, agent MUST:
1. Match this charter's 5×5 table
2. Add individual modifier per position
3. Compute total trim % + cash lift
4. Write separate ledger entry

### Ledger Recording

Write to `regime_transitions.jsonl`:

```json
{
  "date": "2024-XX-XX",
  "from": "Bull_Aligned",
  "to": "Bear_Aligned",
  "confirmation_days": 5,
  "action_taken": "trim 25%",
  "cash_lifted_to": "30%",
  "post_30d_outcome": "correct"
}
```

## Exceptions

- **Regime switch concurrent with major macro event** (Fed rate change, war, pandemic) → PDPC tree **paused**, run emergency fast-track
- **Asset has independent catalyst** (product launch, acquisition) → regime switch doesn't apply to that position

## PDPC Philosophy

Application of "saitekisaku tsuikyu" at the **macro layer**: pre-enumerate all regime switch possibilities → corresponding action tree.

Same spirit as [signal-event-reaction-tree](04-signal-event-reaction-tree.md), but macro layer's time scale is slower and impact larger.

## SHADOW → CONFIRMED Conditions

- Within 60 days, regime switches ≥ 4 times (including minor)
- Correct rate ≥ 75% (action right when looking back 30 days)
- Operator didn't complain "too mechanical"

## Links

- Philosophical source: PDPC saitekisaku tsuikyu (macro layer)
- Companion: [signal-event-reaction-tree](04-signal-event-reaction-tree.md) — signal layer sibling
- Companion: [thesis-failure-mode-tree](07-thesis-failure-mode-tree.md) — §macro mode 細化
- Meta: [promotion-demotion-meta](01-promotion-demotion-meta.md)

---
---

# 中文版本

# Macro Regime 切換 PDPC

Macro regime 切換 MUST 走預先窮舉的反應樹，不靠每次臨場判。

## Why

Macro regime 切換是**低頻高影響事件**（年 2-4 次大切換）：
- Bull → Bear 切換時最容易 panic
- Bear → Bull 反向時容易錯過
- 每次 agent「重新想」對策 → 同樣切換不同 session 不同建議

PDPC 解法：預先窮舉「**regime × 切換方向 × position class**」對應動作。

## Regime 5 大類分群

依你的 macro framework 簡化分群（範例用 5 類，可改 13/24/N 類）：

| 群 | 說明 | macro 意義 |
|---|---|---|
| **🟢 Bull Aligned** | 多方一致 | 明確多方 |
| **🟡 Bull Recover** | 自 bear 復原中 | 動能轉正 |
| **⚪ Neutral** | Sideways / Choppy | 無明確方向 |
| **🟠 Bear Recover** | bear 內反彈 | 假反彈風險 |
| **🔴 Bear Aligned** | 空方一致 | 明確空方 |

## 5×5 切換反應 PDPC 樹

```
From → To             | 反應強度 | Position 動作
─────────────────────┼─────────┼──────────────────────────────
🟢 Bull → 🟡 Recover  | 弱信號  | 觀察，無動作
🟢 Bull → ⚪ Neutral  | 中信號  | Core trim 10%, watchlist 清掉
🟢 Bull → 🟠 Bear Rec | 強信號  | Core trim 25%, 全收 watchlist
🟢 Bull → 🔴 Bear     | 極強   | Core trim 50%, cash 提到 30%+
🟡 Recover → 🟢 Bull  | 加碼信號| Watchlist 換 core，加碼 5-10%
🟡 → 🔴 Bear          | 反轉警報| Core trim 33%, cash 至 25%+
⚪ Neutral → 🟢 Bull   | 加碼   | Watchlist 加碼 50%
⚪ Neutral → 🔴 Bear   | 防守   | Core trim 15%, cash 20%+
🟠 Bear Rec → 🟢 Bull  | 反轉確認| 大膽加碼，core 倉位回 80%+
🟠 Bear Rec → 🔴 Bear  | 假反彈  | Trim 防守，cash 30%+
🔴 Bear → 🟠 Recover  | 嘗試底  | 觀察，1/3 加碼 watchlist
🔴 Bear → 🟡 Recover  | 復甦   | Core 倉位從 40% 回 60-70%
🔴 Bear → 🟢 Bull     | 牛市再臨| 全力加碼，cash 降到 5-10%
```

**同 bucket 內微切換**不算大切換，hold 不動。

## Asset Modifier (×3 細分)

Regime 切換不必對每個 position 一視同仁。看個 asset state：

| Asset 狀態 | modifier |
|---|---|
| **強動能 + 上升趨勢** | 切換動作 **減半**（asset 強，hold 多一陣）|
| **弱動能 + 下降趨勢** | 切換動作 **加倍**（asset 弱，加速 trim）|
| **中間狀態** | 走表 |

## 切換確認規則（避免 whipsaw）

PDPC 觸發 MUST 滿足：

1. Regime 切換**連續 5 個交易日確認**（不是單日跳）
2. 並非 earnings 季中（避免事件干擾）
3. Volatility index 對應方向（Bull → Bear 切換 VIX 必須上升）

任一條件不滿足 → 標記 `pending confirm`，14 天後重檢。

## How to apply

### Daily cron

`daily_regime_monitor.py`：
- 每日 EOD 抓當下 regime
- 對比 5 日前 regime
- 若切換 → 跑「切換確認規則」3 題
- 全過 → inbox alert：「Regime 從 {A} 切到 {B}，PDPC 樹建議：{動作}」

### Agent 觸發

Regime 切換 alert 後 agent MUST：
1. 對照本條 5×5 表
2. 對每個 position 加 individual modifier
3. 算出總 trim 比例 + cash 提升
4. 寫單獨 ledger entry

### Ledger 紀錄

寫到 `regime_transitions.jsonl`:

```json
{
  "date": "2024-XX-XX",
  "from": "Bull_Aligned",
  "to": "Bear_Aligned",
  "confirmation_days": 5,
  "action_taken": "trim 25%",
  "cash_lifted_to": "30%",
  "post_30d_outcome": "correct"
}
```

## 例外

- **Regime 切換同期 + 重大 macro 事件**（Fed 利率變、戰爭、疫情）→ PDPC 樹**暫停**，走 emergency fast-track
- **Asset 有獨立 catalyst**（產品發表、收購）→ regime 切換對該 position 不適用

## PDPC 哲學

「最適策追究」紀律的 **macro 層**應用：預先窮舉所有 regime 切換可能 → 對應動作樹。

跟 [signal-event-reaction-tree](04-signal-event-reaction-tree.md) 同精神，只是 macro 層的時間尺度更慢、影響更大。

## SHADOW → CONFIRMED 條件

- 60 天內 regime 切換 ≥ 4 次（含小切換）
- 採信率 ≥ 75%（30 天後回望動作正確）
- Operator 沒抱怨「太機械化」

## 連結

- 哲學源頭：PDPC 最適策追究（macro 層）
- 配套：[signal-event-reaction-tree](04-signal-event-reaction-tree.md) — signal 層姊妹
- 配套：[thesis-failure-mode-tree](07-thesis-failure-mode-tree.md) — §macro mode 細化
- Meta：[promotion-demotion-meta](01-promotion-demotion-meta.md)
