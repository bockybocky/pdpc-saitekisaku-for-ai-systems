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
    - correct_rate < 0.50
    - ill-defined ≥ 2
---

# Charter Lifecycle PDPC (Meta Layer)

Unifies the promotion / demotion path tree for all PROVISIONAL charters. **Pre-enumerates** every branch trigger so the agent never improvises.

## Why

Common problem in LLM-based agent systems: rules / charters accumulate, each with its own promotion criteria, no consistent framework:
- Some have hard thresholds, some rely on agent "feeling it"
- Promotion timing unclear
- Demotion is rare (charters usually die from neglect, not review)

PDPC solution: pre-enumerate 4 states + 6 transition actions as a tree.

## 4-State Definition

| State | Meaning | Default Duration |
|---|---|---|
| **DRAFT** | Just drafted, not yet in SHADOW | Must enter SHADOW or be discarded within 7 days |
| **PROVISIONAL** (= SHADOW phase) | Trial period; collect cases | 30 days (domain-ops 60d, meta charter 60d) |
| **CONFIRMED** | Passed upgrade gate; permanent rule | Permanent (unless demotion triggered) |
| **SUSPENDED** | Paused, awaiting re-evaluation | Review within 60 days or formally discard |

## 6 Transition PDPC Tree

```
DRAFT ─┬─ Operator acks within 7d ──→ PROVISIONAL (SHADOW begins)
       └─ no ack in 7d ─────────────→ discarded

PROVISIONAL ─┬─ N cases + correct rate ≥ 80% + 0 ill-defined → CONFIRMED
             ├─ correct rate < 50% ─────────────────────────→ SUSPENDED
             ├─ ≥ 2 ill-defined / contradictory ────────────→ SUSPENDED
             ├─ SHADOW expired + cases < 1 ─────────────────→ SUSPENDED (dormant)
             └─ Operator says "too verbose" 3 times ────────→ SUSPENDED

CONFIRMED ─┬─ ≥ 3 new disconfirming cases + Operator ack ──→ SUSPENDED (rare)
           └─ Violates upstream charter ─────────────────→ SUSPENDED (auto supersede)

SUSPENDED ─┬─ Operator revives within 60d + new cases ───→ PROVISIONAL (reset SHADOW)
           └─ no revive in 60d ──────────────────────────→ archived
```

## Upgrade Gate Table by Charter Type (pre-enumerated)

| Charter Type | Case Threshold | Correct Rate | SHADOW Period | Example |
|---|---|---|---|---|
| **Security rule** | 1 (single exposure = promote) | 100% (zero tolerance) | 0d (direct CONFIRMED) | `no_secret_dump` |
| **Academic rule** (well-established principle) | 1 + 2 cross-vendor red team catches | 100% | 0d | `overlapping_returns_require_newey_west` |
| **Methodology charter** | 3 | 80% | 30d | `cross_vendor_redteam_saves_blind_spots` |
| **Execution discipline charter** | 5 | 70% | 30d | `borrow_then_localize` / `deterministic_over_llm_rederive` |
| **Meta charter** | 2 (applied to ≥ 2 child charters) | 80% | 60d | this one (charter governance) |
| **Domain SOP** | 4 | 75% | 60d | thesis failure mode / event reaction |
| **Human ops** | 3 | 100% (interpersonal zero-tolerance) | 60d | advice 4-quadrant tree |

## 6 Demotion Triggers (SUSPENDED)

1. **Correct rate < 50%** — charter is failing more than it's helping
2. **≥ 2 ill-defined cases** — cross-case contradictions → problem definition is wrong
3. **SHADOW expired + cases < 1** — no real-world trigger, possibly unnecessary
4. **Operator says "too verbose" 3 times** — anti-UX
5. **≥ 3 new disconfirming cases** — experience refutes the rule
6. **Violates upstream charter** — auto-supersede

## Auto-Review Schedule (PDPC discipline externalized)

- Every PROVISIONAL charter MUST include `shadow_expiry: YYYY-MM-DD` in frontmatter
- Daily cron scans frontmatter; 7 days before expiry, sends inbox alert:
  ```
  ⚠️ Charter expiry warning:
  - borrow-then-localize.md (expiry 2024-06-28, N days left)
  - Cases triggered: M / correct rate: X% / ill-defined: Y
  - Suggestion: promote to CONFIRMED / extend SHADOW / SUSPENDED
  ```
- Operator responds within 7 days → state transitions automatically
- 7 days no response → demote to SUSPENDED awaiting revive

Cron script example: [`../docs/cron_expiry_check.py`](../docs/cron_expiry_check.py).

## Upgrade Gate Check PDPC (5 steps)

Runs automatically at SHADOW expiry:

1. **Count cases**: grep memory dir for `[charter-name]` mentions; exclude "rule itself referenced", count only "real-world triggered"
2. **Compute correct rate**: per case outcome (was the captured judgment validated by later evidence)
3. **Check ill-defined**: any cross-case contradictory advice (accepted R1 then R2 says R1 was wrong)
4. **Match table**: compare against §Upgrade Gate Table by Charter Type
5. **Verdict**: auto-suggest promote / extend / demote; operator responds within 7 days

## How to Apply

### Required frontmatter when writing new charter

```yaml
---
name: ...
description: ...
metadata:
  type: charter / feedback / project / reference
  scope: family / meta / domain / human-ops / signal / macro
  status: PROVISIONAL          # or DRAFT / CONFIRMED / SUSPENDED
  shadow_expiry: 2024-MM-DD    # required, per table
  pdpc_layer: borrow / execute / governance / signal / macro / human
  upgrade_threshold:
    cases: N
    correct_rate: ≥ 0.XX
  downgrade_triggers:
    - correct_rate < 0.50
    - ill-defined ≥ 2
---
```

### Agent behavior

- When mentioning a PROVISIONAL charter, MUST tag accumulated case count (don't wait until expiry to count)
- Each trigger writes to charter's "cases" section
- 7 days before SHADOW expiry, proactively report upgrade gate check
- Don't rely on agent "feeling it" — follow the table

## SHADOW → CONFIRMED Conditions (for this meta charter itself)

- Within 60 days, apply to ≥ 2 child charters (this rule gets referenced + used to decide promote/demote)
- No operator reversal
- Expiry: 2024-XX-XX (meta charter 60d)

## Cases (fill in after adoption)

- (charter adoption date) (charter name) — promoted to CONFIRMED using "methodology charter" row (N cases / X% / 0 ill-defined) ✅ matched this table

## Links

- Philosophical source: PDPC saitekisaku tsuikyu — pre-enumerate + externalize discipline (meta governance layer)
- Companion: [deterministic-over-llm-rederive](03-deterministic-over-llm-rederive.md) — execute layer
- Companion: [borrow-then-localize](02-borrow-then-localize.md) — borrow layer

---
---

# 中文版本

# Charter 升降級 PDPC（Meta 層）

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

## 連結

- 哲學源頭：PDPC 最適策追究 — 預先窮舉 + 紀律外部化（meta governance 層應用）
- 配套：[deterministic-over-llm-rederive](03-deterministic-over-llm-rederive.md) — execute 層
- 配套：[borrow-then-localize](02-borrow-then-localize.md) — borrow 層
