---
name: regime-switch-pdpc
description: PROVISIONAL Charter — Macro regime 切換預先窮舉動作樹，不靠每次臨場判
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
    - Operator 抱怨「太機械化」
---

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
