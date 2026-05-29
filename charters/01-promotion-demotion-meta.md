---
name: charter-promotion-demotion-meta
description: Meta charter for unified PROVISIONAL → CONFIRMED / SUSPENDED lifecycle. Pre-enumerate all transitions so agent never improvises on charter governance.
metadata:
  type: charter
  scope: meta
  status: PROVISIONAL
  shadow_expiry: 2024-XX-XX  # set when adopting
  pdpc_layer: meta_governance
  upgrade_threshold:
    cases: 2  # apply to ≥ 2 child charters
    correct_rate: 0.80
  downgrade_triggers:
    - 採信率 < 0.50
    - ill-defined ≥ 2
---

# Charter Lifecycle PDPC (Meta Layer)

統一所有 PROVISIONAL Charter 的升降級路徑樹，**預先窮舉**每個分叉的觸發條件，**不靠 agent 臨場判**。

## Why

LLM-based agent system 常見問題：rule / charter 越加越多，每條自訂升降級條件，缺一致框架：
- 有些寫死門檻、有些靠 agent 「感覺到了」
- 升級時點不確定
- 降級沒人主動觸發（charter SUSPENDED 案例極少 — 通常死於忽略不是死於 review）

PDPC 解法：把 4 種狀態 + 6 種轉換動作預先窮舉成樹。

## 4 狀態定義

| 狀態 | 意義 | 預設效期 |
|---|---|---|
| **DRAFT** | 草擬中，未明確進入 SHADOW | 7 天內必進 SHADOW 或廢棄 |
| **PROVISIONAL** (= SHADOW 階段) | 試行觀察期，期內收集案例 | 30 天（domain-ops 60 天，meta charter 60 天） |
| **CONFIRMED** | 通過升級閘門，常駐規則 | 永久（除非觸發降級） |
| **SUSPENDED** | 暫停，待重新評估 | 60 天內 review 或正式廢棄 |

## 6 轉換動作 PDPC 樹

```
DRAFT ─┬─ 7d 內 Operator 拍板 ──→ PROVISIONAL（SHADOW 開始）
       └─ 7d 內無 ack ─────────→ 廢棄

PROVISIONAL ─┬─ N 次案例 + 採信率 ≥ 80% + 0 ill-defined → CONFIRMED
             ├─ 採信率 < 50% ─────────────────────────→ SUSPENDED
             ├─ ≥ 2 次 ill-defined / 自相矛盾 ─────────→ SUSPENDED
             ├─ SHADOW 過期 + 案例 < 1 ────────────────→ SUSPENDED（休眠不廢）
             └─ Operator 3 次說「太囉嗦」/「不要」 ────→ SUSPENDED

CONFIRMED ─┬─ ≥ 3 次新案例反證 + Operator ack ──────→ SUSPENDED（罕見）
           └─ 違反更上位 charter ────────────────────→ SUSPENDED（自動 supersede）

SUSPENDED ─┬─ 60d 內 Operator 主動 revive + 新案例 ──→ PROVISIONAL（重置 SHADOW window）
           └─ 60d 內無 revive ──────────────────────→ 廢棄 archive
```

## 各場景升級閘門表（預先窮舉）

| Charter 類型 | N 案例門檻 | 採信率門檻 | SHADOW 期 | 範例 |
|---|---|---|---|---|
| **資安鐵律** | 1（單次暴露即升）| 100%（不容忍）| 0d（CONFIRMED 直接） | `no_secret_dump` |
| **學術鐵律**（公認原則）| 1 + 跨家紅隊 2 抓 | 100% | 0d | `overlapping_returns_require_newey_west` |
| **方法論 charter** | 3 | 80% | 30d | `cross_vendor_redteam_saves_blind_spots` |
| **執行紀律 charter** | 5 | 70% | 30d | `borrow_then_localize` / `deterministic_over_llm_rederive` |
| **Meta charter** | 2（apply 到 ≥ 2 子 charter）| 80% | 60d | 本條（charter governance）|
| **Domain SOP** | 4 | 75% | 60d | thesis failure mode / event reaction |
| **Human ops** | 3 | 100%（人際零容忍）| 60d | advice 4-quadrant tree |

## 6 種觸發降級 SUSPENDED 條件

1. **採信率 < 50%** — charter 失效，本身錯誤多於對
2. **≥ 2 次 ill-defined** — 跨案例自相矛盾 → 問題定義錯
3. **SHADOW 過期 + 案例 < 1** — 沒實戰機會，可能不必要
4. **Operator 3 次說「太囉嗦」** — UX 反人類
5. **≥ 3 新案例反證** — 經驗推翻原規則
6. **違反更上位 charter** — 自動 supersede

## 自動 review 排程（PDPC 紀律外部化）

- 每條 PROVISIONAL charter MUST 含 `shadow_expiry: YYYY-MM-DD` frontmatter
- Daily cron 每天掃 frontmatter，expiry 前 7 天 inbox alert：
  ```
  ⚠️ Charter expiry 警告：
  - borrow-then-localize.md (expiry 2024-06-28, 剩 N 天)
  - 觸發案例：M 次 / 採信率：X% / ill-defined：Y 次
  - 建議：升 CONFIRMED / 延長 SHADOW / SUSPENDED
  ```
- Operator 7 天內回應 → 自動轉換狀態
- 7 天無回應 → 降 SUSPENDED 待 revive

範例 cron script 見 [`../docs/cron_expiry_check.py`](../docs/cron_expiry_check.py).

## 升級閘門檢查 PDPC（5 步）

到 SHADOW expiry 自動跑：

1. **數案例**：grep memory dir 找 `[charter-name]` 出現次數，扣掉「規則本身被引用」只算「實戰觸發」
2. **算採信率**：每個案例的 outcome（採信抓 bug 那家是否事後驗證對）
3. **檢 ill-defined**：是否有跨案例自相矛盾建議（採納 R1 後 R2 反過來說 R1 錯）
4. **比表**：依本條 §「各場景升級閘門表」對照
5. **裁決**：自動建議升 / 延 / 降，Operator 7 天內回應

## How to apply

### 寫新 charter 時 MUST 含

```yaml
---
name: ...
description: ...
metadata:
  type: charter / feedback / project / reference
  scope: meta / domain / human-ops / signal / macro
  status: PROVISIONAL          # or DRAFT / CONFIRMED / SUSPENDED
  shadow_expiry: 2024-MM-DD    # 必填，依本條表
  pdpc_layer: borrow / execute / governance / signal / macro / human
  upgrade_threshold:
    cases: N
    correct_rate: ≥ 0.XX
  downgrade_triggers:
    - 採信率 < 0.50
    - ill-defined ≥ 2
---
```

### Agent 行為

- 提及 PROVISIONAL charter 時 MUST 標記累積案例次數（不要等到 expiry 才數）
- 每觸發一次寫到 charter「案例」section
- SHADOW expiry 前 7 天主動報告升級閘門檢查
- 不靠 agent「感覺到了該升 / 該降」— 走表

## SHADOW → CONFIRMED 條件（本條 meta charter 自己）

- 60 天內 apply 到 ≥ 2 子 charter（本身被引用 + 用閘門表決定升降級）
- 沒 Operator 反悔
- Expiry: 2024-XX-XX（meta charter 60d）

## 案例 section（落地後填）

- (charter adoption date) (charter name) — 升 CONFIRMED 用「方法論 charter」格 (N cases / X% / 0 ill-defined) ✅ 對照本條表標準
- ...

## 連結

- 哲學源頭：PDPC 最適策追究 — 預先窮舉 + 紀律外部化（meta governance 層應用）
- 配套：[deterministic-over-llm-rederive](03-deterministic-over-llm-rederive.md) — execute 層
- 配套：[borrow-then-localize](02-borrow-then-localize.md) — borrow 層
