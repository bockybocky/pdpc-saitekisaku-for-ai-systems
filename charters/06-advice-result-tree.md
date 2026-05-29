---
name: advice-result-tree
description: PROVISIONAL Charter — 4-quadrant result tree (executed/not × good/bad outcome) for advice-giving, with pre-stated 4-quadrant existence to avoid outcome-biased reactions after the fact.
metadata:
  type: feedback
  scope: human-ops
  status: PROVISIONAL
  shadow_expiry: 2024-XX-XX
  pdpc_layer: human
  upgrade_threshold:
    cases: 3
    correct_rate: 1.00  # interpersonal zero-tolerance
  downgrade_triggers:
    - any case follows wrong script → SUSPEND review
---

# Advice 4-Quadrant Result Tree (PDPC Human Ops)

After giving someone advice, 4 possible outcomes are **pre-enumerated with response scripts**. Companion to "pre-advice" SOP — fills in the gap of "how to handle outcomes **after** the advice".

## Why

"Pre-advice" SOP (red-flag detection / three-tier triage / mandatory red team / framework self-check) usually works fine.

**What's missing**: after the advice is given, the other party acts → 4 outcomes → your / their reactions weren't pre-scripted. Common case: give friend advice → they execute → big gain → get treated like a guru (or big loss → get blamed) → **no pre-scripted response, passively accept**.

PDPC solution: 4-quadrant tree pre-enumerates "executed yes/no × outcome good/bad" + response scripts.

## 4-Quadrant Result PDPC Tree

```
                  They executed →        They didn't execute →
              ┌─────────────────────┬─────────────────────┐
   Outcome   │                     │                     │
   Good      │ A1: They profit +    │ A2: They missed +    │
              │     come to you      │     regret            │
              │ Your reaction →     │ Your reaction →      │
              │ "Framework is on    │ "You didn't do it,    │
              │  page X, not the    │  not my concern"     │
              │  target call"       │                     │
              ├─────────────────────┼─────────────────────┤
   Outcome   │                     │                     │
   Bad       │ B1: They lose +      │ B2: They didn't do + │
              │     blame you        │     would have lost  │
              │ Your reaction →     │ Your reaction →      │
              │ "I said at the time │ "Skipping saved you,  │
              │  ① don't know your  │  but next time learn  │
              │     finances        │  the framework"       │
              │  ② don't know risk  │                     │
              │  ③ not responsible  │                     │
              │     for outcome"    │                     │
              └─────────────────────┴─────────────────────┘
```

## Detailed Scripts per Quadrant

### A1: Executed + Good → They come to you (**MOST DANGEROUS, positive reinforcement of wrong lesson**)

**Response**:
1. Don't say "I'm a genius" (you'll be worshipped, next time will be worse)
2. MUST say: "**This was luck, not the framework. Framework is at [link], learn it yourself**"
3. Proactively analyze: was the gain alpha or beta?
4. Remind: "Next time same framework could reverse, would you still do it?"

**Agent proactive suggestion**: give operator a template: "{result} +X% vs benchmark same period +Y%, pure target alpha is X-Y pp, so this was 50% beta. Framework unvalidated, don't treat as repeatable."

### A2: Not Executed + Good → They regret and come to you

**Response**:
1. **Don't feel guilty** (they didn't execute = their decision)
2. "You asked my opinion, I gave a framework, the final call wasn't followed through by you"
3. Reaffirm: "I can't be responsible for your outcomes — neither should you"

**Agent proactive suggestion**: remind operator "lucky this advice was right; next time same pattern may not be" + write ledger marking "not executed + good outcome" case

### B1: Executed + Bad → They blame you (**5-step response**)

1. **Don't argue, soothe emotion first** (when emotion is up, logic doesn't penetrate)
2. Remind: "I said 3 things: ① don't know your finances ② don't know your risk tolerance ③ not responsible for outcome"
3. Pull up original conversation records (grep messaging history)
4. "I can't reimburse you, but I can analyze with you where it went wrong"
5. **Long-term discipline**: with this friend, follow "pre-advice" SOP more strictly next time

**Agent proactive suggestion**: give operator pre-made message templates (3 versions: short/mid/long) + remind "don't try to reimburse, creates bad habit"

### B2: Not Executed + Bad → They're fine (**SAFEST**)

**Response**:
1. "Skipping saved you — but next time learn the framework"
2. Use as teaching moment: "If you had done it, you'd hurt now"
3. Use as opportunity for them to learn

## Ledger Recording (mandatory)

Write to `people/{friend_id}/advice_ledger.jsonl`:

```json
{
  "date": "2024-XX-XX",
  "friend": "alice",
  "target": "XYZ stock",
  "case_at_advice": "Your estimate 70% B 70% C 20% A 10%",
  "executed": true,
  "outcome_30d": "+15.3%",
  "outcome_class": "A1",
  "actual_alpha": "+8.2%",
  "actual_beta": "+7.1%",
  "post_action": "Explained alpha vs beta + didn't claim credit"
}
```

Every advice instance is logged — long-term accumulation feeds correct rate (used by meta charter upgrade gate).

## How to Apply

### After "Pre-Advice" SOP Completes

Run existing "pre-advice" SOP → give advice → **MUST pre-state 4-quadrant existence**:

> "I'll give you framework + two questions, but **upfront**:
> - If you do it and gain, it's luck not my genius
> - If you do it and lose, the 3 things I said (don't know finances / risk / not responsible) I'll stand by
> - If you don't do it regardless of outcome, not my concern
> - My utility isn't gain/loss, it's giving you framework for self-judgment"

Pre-stating = **PDPC discipline externalized**, avoiding outcome-biased reactions later.

### Mental Practice

Before giving any friend advice, self-ask:
1. If A1, what would I say? (don't claim credit + emphasize alpha/beta)
2. If B1, what would I say? (pull original conversation + don't reimburse + don't argue)

Practice through before opening mouth.

## PDPC Philosophy

Application of "saitekisaku tsuikyu" at the **human ops layer**: 4 outcomes after giving interpersonal advice pre-enumerated → response script → discipline externalized.

Unlike financial / signal / macro, **human-ops charter correct rate threshold is 100%** (family / friends zero-tolerance, any wrong-quadrant response = failure).

## SHADOW → CONFIRMED Conditions

(Per meta charter Human ops row — 3 cases + 100% correct rate)

- Within 60 days, triggered ≥ 3 times (friend / family / colleague)
- Correct rate 100%
- Operator wasn't blamed by any friend

## Links

- Philosophical source: PDPC saitekisaku tsuikyu (human ops layer)
- Companion: "pre-advice" SOP (red-flag detection + three-tier triage + red team)
- Meta: [promotion-demotion-meta](01-promotion-demotion-meta.md)

---
---

# 中文版本

# Advice 4-Quadrant Result Tree (PDPC Human Ops)

給別人建議後 4 種可能結果**預先窮舉應對腳本**。配套既有「給建議前」SOP，補完「給建議**後**該怎麼處理結果」這層。

## Why

「給建議前」的 SOP（紅旗詞偵測 / 三層分流 / 強制紅隊 / 框架自檢）通常都做得不錯。

**還沒處理**的是：給完建議後對方執行 → 4 種結果 → 你 / 對方反應預設沒寫。常見案例：給朋友建議 → 對方執行 → 大漲 → 被當神供奉（或大跌被罵）→ **沒預設應對腳本被動承受**。

PDPC 解法：4 格樹預先窮舉「對方執行 yes/no × 結果好/壞」+ 應對腳本。

## 4 格結果 PDPC 樹

```
                對方執行了 →           對方沒執行 →
              ┌─────────────────────┬─────────────────────┐
   結果       │                     │                     │
   好          │  A1: 對方賺 + 找你   │  A2: 對方錯過 + 後悔  │
              │  你反應 →           │  你反應 →           │
              │  「框架在哪頁，不是    │  「你自己沒做，跟我    │
              │   target 對」       │   無關」            │
              ├─────────────────────┼─────────────────────┤
   結果       │                     │                     │
   壞          │  B1: 對方賠 + 罵你   │  B2: 對方沒做 + 賠了  │
              │  你反應 →           │  你反應 →           │
              │  「我當時說 ① 不知    │  「沒做就沒事，但下次  │
              │   你財務 ② 不知風險   │   還是要學框架」     │
              │   ③ 不對結果負責」   │                     │
              └─────────────────────┴─────────────────────┘
```

## 4 格詳細應對腳本

### A1：執行 + 結果好 → 對方來找你（**最危險，正向強化錯**）

**應對**：
1. 不要說「我厲害」（會被當神供奉，下次更慘）
2. 一定要說：「**這次是運氣，不是框架。框架在 [link]，自己學**」
3. 主動分析「這次好的結果是 alpha 還是 beta」
4. 提醒「下次同樣框架可能反向，你還會做嗎？」

**Agent 主動建議**：給 operator 一句模板：「{result} +X% vs benchmark 同期 +Y%，純 target alpha 是 X-Y pp，所以本次 50% 是 beta。框架沒驗證，不要當成可重複」

### A2：沒執行 + 結果好 → 對方後悔來找你

**應對**：
1. **不要愧疚**（對方自己沒執行 = 對方的決定）
2. 「你問我意見，我給框架，最後是你的判斷沒走完」
3. 重申「我不能對你結果負責 — 你也不該」

**Agent 主動建議**：提醒 operator「這次運氣好你建議對，下次同模式不一定」+ 寫 ledger 標記「未執行 + 好結果」case

### B1：執行 + 結果壞 → 對方來罵你（**5 步應對**）

1. **不爭辯，先安撫情緒**（情緒在，講道理沒用）
2. 提醒「我當時說 3 件事：① 不知你財務 ② 不知你風險承受 ③ 不對結果負責」
3. 拿出原話對話紀錄（grep 訊息 history）
4. 「我不能補你錢，但我可以陪你分析錯哪裡」
5. **長期紀律**：以後對這個朋友 follow 「給建議前」SOP 更嚴

**Agent 主動建議**：給 operator 預製訊息模板 3 種（短/中/長）+ 提醒「不要試圖補錢，會養成壞慣性」

### B2：沒執行 + 結果壞 → 對方沒事（**最安全**）

**應對**：
1. 「你沒做就沒事 — 但下次還是要學框架」
2. 順勢教育「如果你當時做了，現在會痛」
3. 把這次當教學機會

## 紀錄 ledger（必做）

寫到 `people/{friend_id}/advice_ledger.jsonl`：

```json
{
  "date": "2024-XX-XX",
  "friend": "alice",
  "target": "XYZ stock",
  "case_at_advice": "你推估 70% B 70% C 20% A 10%",
  "executed": true,
  "outcome_30d": "+15.3%",
  "outcome_class": "A1",
  "actual_alpha": "+8.2%",
  "actual_beta": "+7.1%",
  "post_action": "解釋 alpha vs beta + 不收功勞"
}
```

每次給建議都寫 — 長期累積看採信率（meta charter 升級閘門用）。

## How to apply

### 給建議前 SOP 跑完後

跑完既有「給建議前」SOP → 給建議 → **MUST 預先講 4 格樹存在**：

> 「給你框架 + 兩個問題，但**先告訴你**：
> - 如果你做了好結果，是運氣不是我厲害
> - 如果你做了壞結果，我當時說的 3 件事（不知財務 / 不知風險 / 不負責）我會堅持
> - 如果你沒做不管結果，跟我無關
> - 我的 utility 不是賺賠，是給你框架自己判」

預先講 = **PDPC 紀律外部化**，避免之後 outcome-biased 反應。

### 心理練習

每次給朋友建議前自問：
1. 如果 A1 我會怎麼說？（不收功勞 + 強調 alpha/beta）
2. 如果 B1 我會怎麼說？（拿原話 + 不補錢 + 不爭辯）

預演完才動嘴。

## PDPC 哲學

「最適策追究」紀律的 **human ops 層**應用：人際給建議的 4 種 outcome 全預先窮舉 → 對應腳本 → 紀律外部化。

跟金融 / signal / macro 不同，**人際 charter 採信率門檻是 100%**（家人 / 朋友零容忍，任一格走錯都失敗）。

## SHADOW → CONFIRMED 條件

（依 meta charter Human ops 格 — 3 案例 + 100% 採信率）

- 60 天內觸發 ≥ 3 次（朋友 / 家人 / 同事任一）
- 採信率 100%
- Operator 沒被任何朋友罵

## 連結

- 哲學源頭：PDPC 最適策追究（human ops 層）
- 配套：「給建議前」既有 SOP（紅旗詞偵測 + 三層分流 + 紅隊）
- Meta：[promotion-demotion-meta](01-promotion-demotion-meta.md)
