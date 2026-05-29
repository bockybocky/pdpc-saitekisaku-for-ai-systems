---
name: deterministic-over-llm-rederive
description: PROVISIONAL Charter — 重複性 skill 流程的 logic 部分 MUST 抽成 deterministic script，不靠 LLM 每次 re-derive；SKILL prose 只留 what + when，how 走 script
metadata:
  type: feedback
  scope: execute
  status: PROVISIONAL
  shadow_expiry: 2024-XX-XX
  pdpc_layer: execute
  upgrade_threshold:
    cases: 5
    correct_rate: 0.70
  downgrade_triggers:
    - Operator 抱怨「script 太多管不動」
---

# Deterministic Script > LLM 每次 Re-derive

任何被同一 skill 重複跑 ≥ 5 次的流程 logic，MUST 抽成 deterministic script (Python stdlib-only 為佳)。**SKILL prose 只留 what + when，how 走 script**。

## Why

LLM 每次自己 re-derive 同 logic 會：
- 產生不一致結果（同 input 不同 output）
- 模糊門檻 → 觸發頻率太低或太高
- 寫入路徑無 dedup → 重複資料累積

**真實案例**（業界 OSS 教訓 — fredchu/claude-session-handoff v1.4 CHANGELOG 原文）：

> Duplicate notes root cause. Create/update was LLM-driven raw AppleScript with self-judged "first time vs update", producing duplicate canonical notes over time.

翻譯：靠 LLM「自己判斷第一次 vs update」會製造重複 — write-path 防護**靠 LLM 守紀不夠可靠**。

**解法**：write 全走 deterministic upsert script，dedup sweep 每次 SessionStart 跑。

## 3 條規則

### 規則 1：判別重複性流程的門檻

任何流程符合以下任一條件 → 抽 script：

- 被同一 skill 重複跑 **≥ 5 次** 且 logic 每次相同
- prose 描述含「掃描」「偵測」「判斷是否 ≥ N」「按條件分組」等 deterministic 操作
- 依賴 LLM 自我判斷模糊門檻（「如果有教訓」「值得沉澱」「夠多了」）

### 規則 2：SKILL prose 只留 what + when

prose 該寫：
- ✅ **what**：這 phase 做什麼（一句話）
- ✅ **when**：什麼條件觸發
- ✅ **why**：為什麼這樣做

prose **不該寫**：
- ❌ **how**：具體 logic / 條件判斷 / parser / sort key

how 全部走 script。SKILL prose 寫：

```markdown
### Phase 3：Weekly Consolidation（自動）

archive ≥ 5 條直接跑：

\`\`\`bash
python scripts/count_archive_entries.py
# 若 should_consolidate=true → 直接執行
python scripts/consolidate_archive.py
\`\`\`
```

不寫：「掃整週 Archive，偵測：重複出現的問題 → 建議寫入 MEMORY...」（這種 prose 變成 LLM 每次自己 re-derive）。

### 規則 3：script 設計鐵律

- **stdlib only**：不要 import 第三方 lib（pandas / numpy 等）— LLM tooling 環境可能沒裝
- **single-purpose**：一個 script 做一件事
- **CLI 化**：argparse，可 dry-run，可 --quiet 給 hook 用
- **output JSON**：給下一 script / LLM 機讀

## How to apply

### 觸發掃描

每次 SKILL edit / 新 skill 建立時自問：
1. 這 prose 描述的 logic 會被執行 ≥ 5 次嗎？
2. 條件判斷有確定門檻嗎（數字 / 完全相等 / regex）？
3. 同樣 input 應該產出同樣 output 嗎？

3 題都 yes → 抽 script。

### 範本

stdlib-only script 範本（~50-100 行）：

```python
#!/usr/bin/env python3
"""One-line purpose."""
import argparse, json, sys
from pathlib import Path

def core_logic(data):
    ...
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    result = core_logic(...)
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
```

## PDPC 哲學

「最適策追究」紀律的**執行層**應用：預先窮舉 logic → 寫死 script → 不靠 LLM 臨場 re-derive。

PDPC 樹的執行變體：

```
重複 logic ─┬─ ≥ 5 次同樣 input/output → 抽 deterministic script
            └─ < 5 次 / 每次 context 不同 → 留 LLM prose
```

## SHADOW → CONFIRMED 條件

- 30 天內成功抽 script ≥ 5 次
- 抽完 LLM 觸發率 / 一致性 **明顯提升**（quantifiable proxy：consolidate 觸發次數 / dedup 結果）
- Operator 沒抱怨「script 太多管不動」

## 案例 (真實 OSS 引用，公開 reference)

### Case: fredchu/claude-session-handoff v1.4.0 (2024-05-29)

| Before | After |
|---|---|
| LLM 每次自判「first time vs update」 | `applescript_notes.py write` exact-title upsert |
| 寫入失敗靠 LLM retry | `run_applescript` 自動 retry `-1719`/`-1712`/`-1700` |
| 重複 Notes 累積 | `applescript_notes.py dedup --apply` 每次 SessionStart 跑 |

效果：duplicate root cause 解決。

CHANGELOG 原文: https://github.com/fredchu/claude-session-handoff/blob/main/CHANGELOG.md

## 連結

- 哲學源頭：PDPC 最適策追究（執行層）
- 配套：[borrow-then-localize](02-borrow-then-localize.md) — 移植層姊妹（移植來後 logic 確定化）
- Meta：[promotion-demotion-meta](01-promotion-demotion-meta.md) — 本 charter 自己的 lifecycle
