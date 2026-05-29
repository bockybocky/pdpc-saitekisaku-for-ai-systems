---
name: borrow-then-localize
description: PROVISIONAL Charter — When seeing external repo / library to "integrate into our system", MUST first list 3 tables (original features + latest changes + gap vs local) and give scope options. Forbid blindly cloning the whole thing.
metadata:
  type: feedback
  scope: borrow
  status: PROVISIONAL
  shadow_expiry: 2024-XX-XX
  pdpc_layer: borrow
  upgrade_threshold:
    cases: 3
    correct_rate: 0.80
  downgrade_triggers:
    - Operator says "skip the list, just do it" 3 times → SUSPEND
---

# Borrow Then Localize (Not Direct Clone)

When the operator gives a GitHub URL and says "adapt it to our system / integrate it / port it over", the agent MUST follow a 5-step SOP. **Direct cloning of the whole thing is forbidden.**

## Why

Directly cloning the entire external repo easily hits:
1. **Platform incompatibility** (e.g., macOS-only repo on Windows)
2. **Auth / permission differences**
3. **Architecture conflicts with existing system**
4. **Unused layers becoming dead weight**

But not borrowing at all is also wrong — good repos often hide gems in their design evolution (v1.0 → v1.4) like dedup sweeps, lesson extraction patterns.

**Solution**: spread out + layer + choose scope, then act.

## 5-Step SOP

### 1. Fetch metadata (no clone)

```bash
curl -s https://api.github.com/repos/{owner}/{repo}      # default branch + last update
curl -s https://api.github.com/repos/{owner}/{repo}/commits?per_page=5
curl -s https://raw.githubusercontent.com/.../README.md
curl -s https://raw.githubusercontent.com/.../CHANGELOG.md
```

Only fetch README + CHANGELOG + last 5 commits. **No clone yet.**

### 2. List "Original Features" Table

Break down by version, one row per version — reveals **design evolution**:

```
| Version | Features |
|---|---|
| v1.0 | Core X / Y / Z |
| v1.2 | Added "lesson extraction system" 5 signals + 5 steps |
| v1.4 | Dedup sweep + Python script-ified |
```

### 3. List "Latest Version Additions" Table

Latest CHANGELOG split into Added / Fixed / Changed three columns.

### 4. List "Gap vs Local" Table

For each feature: does local already have it? Platform compatible? Same source paradigm?

```
| External feature | Local has? | Platform compatible? | Fit score |
|---|---|---|---|
| Apple Notes persistence | ❌ | ❌ macOS only | skip |
| Phase 4 5 signals | ❌ Phase 4 is prose-only | ✅ portable | high |
| Dedup sweep | ❌ | ✅ rewrite markdown ver | high |
```

### 5. Present 3-4 Scope Options + Recommendation

```
A. Full port (4 items + rewrite local-compatible version)
B. High-ROI subset only (lesson extraction + dedup sweep)
C. Just learn the methodology, don't import
D. Skip entirely (functionality too different from local)

Recommended: B — XXX fills local weakness + YYY is a safety net
```

## How to Apply

**Trigger phrases**:
- "Update {github URL}" (still "for our system" context, not pure fetch)
- "Adapt this to our system"
- "Integrate {repo}"
- "Port {repo} over"
- "Import {repo}"

**Forbidden**:
- ❌ Direct `git clone` of the whole thing locally
- ❌ Skip metadata, jump to reading main files
- ❌ Don't list gap table, just pick

**Exceptions** (don't trigger this SOP):
- "Fetch {URL} for me to look at" / "summarize" = pure fetch, no import
- "Pull latest of {URL}" = already a local fork, pure git pull
- "Install {URL} skill" + owner is plugin marketplace = pure install

## PDPC Philosophy

Application of "saitekisaku tsuikyu" discipline at the **borrow layer**: pre-enumerate gap → scope options → don't blindly import.

PDPC tree borrow-variant:

```
See external repo ─┬─ Pure exploration ("fetch for me") ──→ Pure fetch, no import
                   ├─ Integration context ("adapt to our system") ──→ Run 5-step SOP
                   │   └─ After gap table eval ──┬─ Full port (A)
                   │                              ├─ High-ROI subset (B)  ← usually recommended
                   │                              ├─ Learn methodology only (C)
                   │                              └─ Skip entirely (D)
                   └─ Local fork exists ────────→ Pure git pull
```

## SHADOW → CONFIRMED Conditions

- Within 30 days, triggered ≥ 3 times + each time completed 5-step SOP + Operator didn't complain "too verbose"
- Demotion: Operator says "skip the list, just do it" 3 times → SUSPEND

## Cases (fill in after adoption)

- 2024-XX-XX (repo URL): Operator gave URL → ran 5-step → recommended B → avoided platform pitfall

## Links

- Philosophical source: PDPC saitekisaku tsuikyu (borrow layer)
- Companion: [deterministic-over-llm-rederive](03-deterministic-over-llm-rederive.md) — execute layer (post-borrow logic determinism)
- Meta: [promotion-demotion-meta](01-promotion-demotion-meta.md)

---
---

# 中文版本

# 借鏡 → 在地化（不是直接 clone）

Operator 給 GitHub URL + 說「改成我們系統可以用 / 整合進來 / 移植過來」時，agent MUST 走 5 步 SOP，**禁直接 clone 整套**。

## Why

直接 clone 整套外部 repo 容易踩：
1. **平台不相容**（e.g., macOS-only repo 跑 Windows）
2. **認證 / 權限差異**
3. **既有架構衝突**
4. **用不到的 layer 拖累**

但完全不借鏡也錯 — 好 repo 的設計演進（v1.0 → v1.4）裡常藏寶藏（dedup sweep / 教訓萃取 5 訊號等模式）。

**解法**：先攤開 + 分層 + 範圍選 再做。

## 5 步 SOP

### 1. Fetch metadata（不 clone）

```bash
curl -s https://api.github.com/repos/{owner}/{repo}      # default branch + last update
curl -s https://api.github.com/repos/{owner}/{repo}/commits?per_page=5
curl -s https://raw.githubusercontent.com/.../README.md
curl -s https://raw.githubusercontent.com/.../CHANGELOG.md
```

只抓 README + CHANGELOG + 最近 5 commits，**不 clone**。

### 2. 列「原有功能」表

按版本拆，每版一行 — 看出**設計演進**：

```
| 版本 | 功能 |
|---|---|
| v1.0 | 核心 X / Y / Z |
| v1.2 | 新增「教訓萃取系統」5 訊號 + 5 步 |
| v1.4 | dedup sweep + Python script 化 |
```

### 3. 列「最新版新增」表

最新 CHANGELOG 那段拆 Added / Fixed / Changed 三欄。

### 4. 列「跟本地 gap」表

每個功能比對：本地有沒有？平台跑得了？同源嗎？

```
| 外部功能 | 本地有？ | 平台可用？ | 適合度 |
|---|---|---|---|
| Apple Notes 持久層 | ❌ | ❌ macOS only | 跳過 |
| Phase 4 5 訊號 | ❌ Phase 4 只 prose | ✅ 可移 | 高 |
| dedup sweep | ❌ | ✅ 改 markdown 版 | 高 |
```

### 5. 給 3-4 範圍選項 + 推薦

```
A. 全移植（4 件 + 改寫本地相容版）
B. 只移高 ROI 兩件（教訓萃取 + dedup sweep）
C. 只看設計學方法論，不導入
D. 全跳過（功能跟本地差太多）

推薦 B — XXX 補本地弱點 + YYY 是安全網
```

## How to apply

**觸發詞**：
- 「更新 {github URL}」（仍是「我們系統用」語境，不是純 fetch）
- 「改成我們系統可以用的」
- 「整合 {repo} 進來」
- 「移植 {repo} 到我們這邊」
- 「導入 {repo}」

**禁**：
- ❌ 直接 `git clone` 整套到本地
- ❌ 跳過 metadata 直接 read 主檔開做
- ❌ 不列 gap 表直接挑選

**例外**（不觸發此 SOP）：
- 「fetch {URL} 給我看」/「summary 一下」= 只 fetch 不導入
- 「拉 {URL} 最新版」= 已是本地 fork，純 git pull
- 「裝 {URL} skill」+ owner 是 plugin 主流 marketplace = 純 install

## PDPC 哲學

「最適策追究」紀律的**移植層**應用：預先窮舉 gap → 範圍選項 → 不盲目導入。

PDPC 樹的移植變體：

```
看到外部 repo ─┬─ 純探索 (「fetch 給我看」) ──→ 純 fetch，不導入
              ├─ 整合語境 (「改成我們系統用」) ──→ 走 5 步 SOP
              │   └─ gap 表評估後 ──┬─ 全移植 (A)
              │                     ├─ 高 ROI 子集 (B)  ← 通常推薦
              │                     ├─ 只學方法論 (C)
              │                     └─ 全跳過 (D)
              └─ 本地 fork 已存在 ───→ 純 git pull
```

## SHADOW → CONFIRMED 條件

- 30 天內觸發 ≥ 3 次 + 每次都跑完 5 步 SOP + Operator 沒抱怨「太囉嗦」
- 違反條件：Operator 3 次說「不用列表直接做」→ SUSPEND

## 案例 section（落地後填）

- 2024-XX-XX (repo URL)：Operator 給 URL → 走 5 步 → 推薦 B → 沒踩平台陷阱

## 連結

- 哲學源頭：PDPC 最適策追究（移植層）
- 配套：[deterministic-over-llm-rederive](03-deterministic-over-llm-rederive.md) — execute 層（移植後 logic 確定化）
- Meta：[promotion-demotion-meta](01-promotion-demotion-meta.md) — 本 charter 自己的 lifecycle
