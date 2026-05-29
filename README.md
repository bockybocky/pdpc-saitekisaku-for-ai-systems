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
| [charter-promotion-demotion-meta](charters/01-promotion-demotion-meta.md) | 每條 charter 自己訂條件，缺一致框架 | Meta governance |
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
