# 🎯 PDPC Saitekisaku Tsuikyu for AI Systems

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Charters](https://img.shields.io/badge/charters-7-blue.svg)](charters/)
[![Bilingual](https://img.shields.io/badge/docs-EN%20%2F%20中文-green.svg)](#中文版本)
[![Philosophy](https://img.shields.io/badge/origin-PDPC%201979-orange.svg)](https://en.wikipedia.org/wiki/Seven_management_and_planning_tools)
[![Status](https://img.shields.io/badge/status-PROVISIONAL-yellow.svg)](#)

> 🇯🇵 Japanese QC discipline **"Saitekisaku Tsuikyu"** (最適策追究 / pursuit of optimal countermeasures) applied to govern decisions, signals, and execution in AI agent systems.

**PDPC** (Process Decision Program Chart) — one of the 7 New QC Tools formalized by **Mizuno Shigeru in 1979**. Core verb is **追究 (tsuikyu / pursuit)**: exhaustively interrogate every failure mode until an optimal countermeasure is found.

A cousin of FMEA / FTA / Decision Tree, but with stronger emphasis on **dynamic replan + discipline externalization**.

> [!TIP]
> **TL;DR**: Your LLM agent's rules keep accumulating but no one reviews them. Your charter promotion criteria are inconsistent. Your agent re-derives the same logic differently each turn. This repo gives you a battle-tested 4-state lifecycle + 7 reusable charters to govern all of that.

---

## 📋 Table of Contents

- [Why AI Agent Systems Need This](#-why-ai-agent-systems-need-this)
- [7 Charters Included](#-7-charters-included)
- [4 States + 6 Transitions PDPC Tree](#-4-states--6-transitions-pdpc-tree-meta-charter-core)
- [How to Use](#-how-to-use)
- [Philosophical Sources](#-philosophical-sources)
- [License](#-license)
- [中文版本](#中文版本)

---

## 💡 Why AI Agent Systems Need This

Common LLM-based agent problems (you've probably hit all of these):

| Problem | PDPC Solution |
|---|---|
| 🔁 Agent re-derives same logic each time and gets inconsistent results | Freeze deterministic logic into rules / scripts; forbid LLM from re-thinking each turn |
| 📥 Agent blindly clones external repo and hits platform pitfalls | "Borrow then localize" discipline: fork to local, review per-component |
| 📜 Charters / rules accumulate but no one reviews them | Unified promotion / demotion gates (PROVISIONAL → CONFIRMED / SUSPENDED) + daily cron expiry alert |
| 🚨 Red-flag signal fires but human brain freezes in the moment | Pre-enumerate 4-branch PDPC tree, follow the tree instead of improvising |

> [!IMPORTANT]
> **Core principle**: discipline lives **outside** (in charters / rules / cron jobs), not inside the agent's "intuition this turn".

---

## 📚 7 Charters Included

**Architecture layers** (top governs all below):

```
🟡 META GOVERNANCE
   └── 01. promotion-demotion-meta  ← Sets the rules for all other charters
       │
       ├── 🔵 BORROW / EXECUTE
       │   ├── 02. borrow-then-localize        (when bringing external repos in)
       │   └── 03. deterministic-over-llm-rederive  (when extracting reusable logic)
       │
       ├── 🟢 SIGNAL / MACRO
       │   ├── 04. signal-event-reaction-tree  (high-freq events: earnings / FOMC)
       │   └── 05. regime-switch-pdpc          (low-freq macro transitions)
       │
       ├── 🩷 HUMAN OPS
       │   └── 06. advice-result-tree          (4-quadrant after-advice scripts)
       │
       └── 🟣 DOMAIN SOP
           └── 07. thesis-failure-mode-tree    (pre-enumerate how thesis dies)
```

| # | Charter | Problem Solved |
|---|---|---|
| 1 | 🟡 [promotion-demotion-meta](charters/01-promotion-demotion-meta.md) | Each charter sets its own promotion criteria; no consistent framework |
| 2 | 🔵 [borrow-then-localize](charters/02-borrow-then-localize.md) | Blindly cloning external repos creates platform / architecture mismatches |
| 3 | 🔵 [deterministic-over-llm-rederive](charters/03-deterministic-over-llm-rederive.md) | LLM re-deriving same logic each turn → inconsistent results |
| 4 | 🟢 [signal-event-reaction-tree](charters/04-signal-event-reaction-tree.md) | High-frequency signal events (e.g., earnings) reacted to ad-hoc |
| 5 | 🟢 [regime-switch-pdpc](charters/05-regime-switch-pdpc.md) | Regime change reactions not pre-codified |
| 6 | 🩷 [advice-result-tree](charters/06-advice-result-tree.md) | 4 possible outcomes after giving advice not pre-thought |
| 7 | 🟣 [thesis-failure-mode-tree](charters/07-thesis-failure-mode-tree.md) | Thesis failure modes not pre-enumerated |

Every charter is an instance of the same principle: **pre-enumerate + externalize discipline**.

---

## 🔄 4 States + 6 Transitions PDPC Tree (Meta Charter Core)

Every charter runs through a 4-state lifecycle:

| State | Meaning | Duration |
|---|---|---|
| 📝 **DRAFT** | Just drafted, not yet in SHADOW | 7 days to PROVISIONAL or discard |
| 🟡 **PROVISIONAL** | Trial period (= SHADOW phase) | 30-60 days (per layer) |
| 🟢 **CONFIRMED** | Passed gate, permanent rule | Permanent (until demoted) |
| 🔴 **SUSPENDED** | Paused, awaiting re-evaluation | 60d review window |

**Transitions** (pre-enumerated, agent never improvises):

```
📝 DRAFT
   ├─ Operator acks in 7d ──────────────────────→ 🟡 PROVISIONAL
   └─ no ack in 7d ─────────────────────────────→ ❌ discarded

🟡 PROVISIONAL (= SHADOW phase, 30-60d trial)
   ├─ N cases + correct rate ≥ 80% + 0 ill-defined → 🟢 CONFIRMED
   ├─ correct rate < 50% ─────────────────────────→ 🔴 SUSPENDED
   ├─ ≥ 2 ill-defined / contradictory ────────────→ 🔴 SUSPENDED
   ├─ SHADOW expired + cases < 1 ─────────────────→ 🔴 SUSPENDED (dormant)
   └─ Operator says "too verbose" 3 times ────────→ 🔴 SUSPENDED

🟢 CONFIRMED (permanent, but demotable)
   ├─ ≥ 3 new disconfirming + Operator ack ───────→ 🔴 SUSPENDED (rare)
   └─ Violates upstream charter ──────────────────→ 🔴 SUSPENDED (auto supersede)

🔴 SUSPENDED (paused, 60d review window)
   ├─ Operator revives in 60d + new evidence ─────→ 🟡 PROVISIONAL (reset SHADOW)
   └─ no revive in 60d ───────────────────────────→ ❌ archived
```

---

## 🚀 How to Use

### 1️⃣ Fork charters into your agent system's memory

Each charter is markdown + YAML frontmatter. Drop them into your agent memory dir (Claude Code: `~/.claude/projects/.../memory/`; other agent runtimes similarly).

### 2️⃣ Schedule a daily cron for expiry checks

Every PROVISIONAL charter has `shadow_expiry: YYYY-MM-DD` in frontmatter. Cron scans daily, alerts 7 days before expiry:

```
⚠️ Charter expiry warning:
- borrow-then-localize.md (expiry 2024-06-28, 7 days left)
- Cases triggered: 3 / correct rate: 85% / ill-defined: 0
- Suggestion: promote to CONFIRMED
```

Cron script example: [`docs/cron_expiry_check.py`](docs/cron_expiry_check.py) — stdlib-only Python, runs anywhere.

### 3️⃣ Use the template when writing new charters

See [`docs/CHARTER_TEMPLATE.md`](docs/CHARTER_TEMPLATE.md). Every charter MUST include:
- `shadow_expiry`
- `pdpc_layer`
- `upgrade_threshold` (cases / correct_rate)
- `downgrade_triggers`

> [!WARNING]
> Don't write prose describing deterministic logic — extract logic into script; prose only writes **what** + **when** + **why**. See [`charters/03-deterministic-over-llm-rederive.md`](charters/03-deterministic-over-llm-rederive.md) for the rationale.

---

## 📖 Philosophical Sources

| Reference | Why It Matters |
|---|---|
| Mizuno Shigeru 1979 *Management for Quality Improvement: The 7 New QC Tools* | PDPC originating book |
| Rother 2009 *Toyota Kata* | Western codification of Improvement Kata / Coaching Kata |
| Ohno 1988 *Toyota Production System* | Source of 5 Why |
| Asakawa《なぜなぜ分析 実践編》 | Japanese 5 Why practical edition |

PDPC is in the same family as **Toyota TBP**, **5 Why**, **A3 Problem Solving**, **FMEA**, **OODA loop**. This repo focuses on the **discipline of pursuit itself**, not tool minutiae.

---

## 📄 License

MIT — free to use / fork / modify / commercial use.

---

## 🌱 Origin

This repo was extracted from [@bockybocky](https://github.com/bockybocky)'s personal AI agent system memory. The original system contained financial domain-specific context; this repo has been generic-ized to remove any trader / asset / strategy specifics.

> [!NOTE]
> If your agent system suffers from "rules accumulate but governance breaks down", the PDPC 4-state + 7-charter pattern should help.

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=bockybocky/pdpc-saitekisaku-for-ai-systems&type=Date)](https://star-history.com/#bockybocky/pdpc-saitekisaku-for-ai-systems&Date)

---

## 🤝 Contributing

Issues + PRs welcome. If you adopt these charters in your own agent system and have lessons learned, please share via Issue.

---

*🇯🇵 PDPC Saitekisaku Tsuikyu — write the pursuit discipline into the AI agent system, don't rely on in-the-moment improvisation.*

---
---

# 中文版本

# PDPC 最適策追究 for AI Systems

> 用日本品管「最適策追究」紀律，治理 AI Agent 系統的決策、信號、執行流程

**PDPC** (Process Decision Program Chart, 過程決策程序圖) — 1979 年水野滋為日本品管七大新手法之一。核心動詞「**追究**」(さいてきさく ついきゅう)：對每個 failure mode 窮舉式逼問到「最適策」為止。

跟 FMEA / FTA / Decision Tree 是堂兄弟，但更強調**動態 replan + 紀律外部化**。

---

## 為什麼 AI Agent 系統需要這個

LLM-based agent 常見毛病（你大概都遇過）：

| 問題 | PDPC 解法 |
|---|---|
| Agent 每次 re-derive 同 logic 得到不一致結果 | 把確定的 logic 凍結成 deterministic rule，禁 LLM 每次重想 |
| 看到外部 repo 盲目 clone 踩平台陷阱 | 「先借後本地化」紀律，原始碼 fork 一份本地審 |
| Charter / rule 越加越多但沒人 review | 統一升降級閘門（PROVISIONAL → CONFIRMED / SUSPENDED）+ daily cron expiry alert |
| 紅旗訊號出來但人腦當下糾結 | 預先窮舉 4 分支 PDPC 樹，按樹走不靠臨場判 |

**核心精神**：紀律寫在外部（charter / rule / cron），不靠 agent「感覺到了」。

---

## 7 條 Charter (本 repo 收的)

| Charter | 解決問題 | Layer |
|---|---|---|
| [promotion-demotion-meta](charters/01-promotion-demotion-meta.md) | 每條 charter 自己訂條件，缺一致框架 | Meta governance |
| [borrow-then-localize](charters/02-borrow-then-localize.md) | 外部 repo 盲目 clone 踩平台陷阱 | Borrow / Execute |
| [deterministic-over-llm-rederive](charters/03-deterministic-over-llm-rederive.md) | LLM 每次 re-derive 同 logic 不一致 | Borrow / Execute |
| [signal-event-reaction-tree](charters/04-signal-event-reaction-tree.md) | 重大事件（e.g., earnings call）反應 logic 沒預先窮舉 | Signal layer |
| [regime-switch-pdpc](charters/05-regime-switch-pdpc.md) | Regime change 切換策略沒預先 codify | Macro layer |
| [advice-result-tree](charters/06-advice-result-tree.md) | 給人建議的 4 種 outcome 沒預先想清楚 | Human ops |
| [thesis-failure-mode-tree](charters/07-thesis-failure-mode-tree.md) | Thesis 失敗模式沒預先窮舉 | Domain SOP |

每條 charter 都是「**預先窮舉 + 紀律外部化**」精神的 instance。

---

## 4 狀態 + 6 轉換 PDPC 樹（Meta charter 核心）

每條 charter 走 4 狀態 lifecycle：

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

SUSPENDED ─┬─ 60d 內 Operator 主動 revive + 新案例 ──→ PROVISIONAL（重置 SHADOW）
           └─ 60d 內無 revive ──────────────────────→ 廢棄 archive
```

---

## 怎麼用

### 1. 直接 fork charter 進你的 agent system memory

各 charter 是 markdown + YAML frontmatter，直接放進 agent memory dir（Claude Code: `~/.claude/projects/.../memory/`；其他 agent runtime 同理）。

### 2. 設 daily cron 跑 expiry check

每個 PROVISIONAL charter frontmatter 含 `shadow_expiry: YYYY-MM-DD`。Cron 每天掃，expiry 前 7 天 inbox alert：

```
⚠️ Charter expiry 警告：
- borrow-then-localize.md (expiry 2024-06-28，剩 7 天)
- 觸發案例：3 次 / 採信率：85% / ill-defined：0 次
- 建議：升 CONFIRMED
```

Cron script 範例見 [`docs/cron_expiry_check.py`](docs/cron_expiry_check.py)。

### 3. 寫新 charter 時用 template

見 [`docs/CHARTER_TEMPLATE.md`](docs/CHARTER_TEMPLATE.md)。每條 charter MUST 含：
- `shadow_expiry`
- `pdpc_layer`
- `upgrade_threshold` (cases / correct_rate)
- `downgrade_triggers`

---

## 哲學源頭

| 文獻 | 為什麼重要 |
|---|---|
| 水野滋 1979《管理のための新 QC 七つ道具》 | PDPC 創始書 |
| Rother 2009 *Toyota Kata* | 西方對 Improvement Kata / Coaching Kata 紀律化 |
| Ohno 1988 *Toyota Production System* | 5 Why 源頭 |
| Asakawa《なぜなぜ分析 実践編》 | 日文 5 Why 真因追求實踐 |

PDPC 跟 **Toyota TBP**, **5 Why**, **A3 Problem Solving**, **FMEA**, **OODA loop** 是同 family。本 repo 聚焦「**追究紀律本身**」而非工具細節。

---

## License

MIT License — 自由使用 / fork / 修改 / 商用。

---

## 來源

本 repo 從 [@bockybocky](https://github.com/bockybocky) 個人 AI agent system memory 提取。原系統含 financial domain-specific context，本 repo 已 generic 化移除任何特定 trader / asset / strategy 細節。

如果你的 agent 系統有類似「越加越多 rule 但治理失控」的問題，PDPC 4 狀態 + 7 charter pattern 應該對你有用。

---

*PDPC 最適策追究 — 把追究紀律寫進 AI agent 系統，不靠當下臨場想。*
