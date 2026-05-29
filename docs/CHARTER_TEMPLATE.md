# Charter Template

Template for writing new charters. Every charter should follow the same frontmatter + structure.

## Frontmatter

```yaml
---
name: charter-short-name  # kebab-case
description: PROVISIONAL/CONFIRMED Charter — one-line description of what this charter solves
metadata:
  type: charter / feedback / project / reference  # 4 categories
  scope: meta / domain / human-ops / signal / macro / borrow / execute  # PDPC layer
  status: DRAFT / PROVISIONAL / CONFIRMED / SUSPENDED
  shadow_expiry: 2024-MM-DD  # required for PROVISIONAL (DRAFT must → PROVISIONAL within 7d)
  pdpc_layer: same as scope
  upgrade_threshold:
    cases: N  # need N real-world cases
    correct_rate: ≥ 0.XX  # correct rate threshold
  downgrade_triggers:
    - correct_rate < 0.50
    - ≥ 2 ill-defined cases
    - Operator says "too verbose" 3 times
---
```

## 7-Scenario Upgrade Gate Table (per meta charter)

| Charter Type | N Cases | Correct Rate | SHADOW Period |
|---|---|---|---|
| Security rule | 1 | 100% | 0d |
| Academic rule | 1 + 2 cross-vendor red team | 100% | 0d |
| Methodology | 3 | 80% | 30d |
| Execution discipline | 5 | 70% | 30d |
| Meta | 2 child charters | 80% | 60d |
| Domain SOP | 4 | 75% | 60d |
| Human ops | 3 | 100% (zero tolerance) | 60d |

## Required Sections

```markdown
# {Charter Name}

One-line TL;DR

## Why

Why this charter is necessary (problem statement + real case)

## {Core PDPC Tree / N Rules}

Pre-enumerate all cases → corresponding action

## How to apply

- Trigger phrases / scenarios
- Exceptions (not triggered)
- Templates (script template / message template)

## PDPC Philosophy

One sentence describing how this charter relates to the "saitekisaku tsuikyu" discipline at the {layer} layer

## SHADOW → CONFIRMED Conditions

Fill per the upgrade gate table

## Cases (fill in after adoption)

- 2024-XX-XX (case description) — outcome class (correct / ill-defined / failed)

## Links

- Philosophical source: PDPC saitekisaku tsuikyu
- Companion: [other-charter](XX-other-charter.md)
- Meta: [promotion-demotion-meta](01-promotion-demotion-meta.md)
```

## Writing Rules

1. **Don't write prose describing deterministic logic** — extract logic into script; prose only writes what + when + why
2. **Pre-enumerate cases** — don't rely on agent in-the-moment improvisation
3. **Add ledger** — every trigger writes JSONL, upgrade gate review counts them
4. **Link to other charters** — use wikilink or markdown link

---
---

# 中文版本

# Charter Template

寫新 charter 用這個 template。每條 charter 都該走相同 frontmatter + 結構。

## Frontmatter

```yaml
---
name: charter-short-name  # kebab-case
description: PROVISIONAL/CONFIRMED Charter — 一句話講這 charter 解什麼問題
metadata:
  type: charter / feedback / project / reference  # 4 種類別
  scope: meta / domain / human-ops / signal / macro / borrow / execute  # PDPC layer
  status: DRAFT / PROVISIONAL / CONFIRMED / SUSPENDED
  shadow_expiry: 2024-MM-DD  # PROVISIONAL 必填（DRAFT 7d 內 → PROVISIONAL）
  pdpc_layer: same as scope
  upgrade_threshold:
    cases: N  # 需要 N 個實戰案例
    correct_rate: ≥ 0.XX  # 採信率門檻
  downgrade_triggers:
    - 採信率 < 0.50
    - ≥ 2 ill-defined cases
    - Operator 3 次說「太囉嗦」
---
```

## 7 場景升級閘門表（依 meta charter）

| Charter 類型 | N 案例 | 採信率 | SHADOW 期 |
|---|---|---|---|
| 資安鐵律 | 1 | 100% | 0d |
| 學術鐵律 | 1 + 跨家紅隊 2 | 100% | 0d |
| 方法論 | 3 | 80% | 30d |
| 執行紀律 | 5 | 70% | 30d |
| Meta | 2 子 charter | 80% | 60d |
| Domain SOP | 4 | 75% | 60d |
| Human ops | 3 | 100% (零容忍) | 60d |

## 必含 sections

```markdown
# {Charter Name}

一句話精華 (TL;DR)

## Why

為什麼這 charter 必要 (problem statement + 真實案例)

## {核心 PDPC 樹 / N 條規則}

預先窮舉 所有 case → 對應 action

## How to apply

- 觸發詞 / 觸發場景
- 例外 (不觸發)
- 範本 (script template / message template)

## PDPC 哲學

「最適策追究」紀律的 {layer} 應用：一句話描述本 charter 跟 PDPC 的關係

## SHADOW → CONFIRMED 條件

依升級閘門表填

## 案例 section (落地後填)

- 2024-XX-XX (case description) — outcome class (correct / ill-defined / failed)

## 連結

- 哲學源頭：PDPC 最適策追究
- 配套：[other-charter](XX-other-charter.md)
- Meta：[promotion-demotion-meta](01-promotion-demotion-meta.md)
```

## 寫作鐵律

1. **不寫 prose 描述 deterministic logic** — logic 抽 script，prose 只留 what + when + why
2. **預先窮舉 case** — 不靠 agent 臨場判
3. **加 ledger** — 每次觸發寫 JSONL，升級閘門 review 時數
4. **連結其他 charter** — 用 wikilink 或 markdown link
