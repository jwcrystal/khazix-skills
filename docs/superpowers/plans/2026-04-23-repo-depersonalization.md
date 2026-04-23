# Repo Depersonalization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove persona branding from this repository while keeping the repo name unchanged and renaming the `khazix-writer` skill to `longform-writer`.

**Architecture:** Keep the repo structure stable except for the `khazix-writer/` → `longform-writer/` path rename. Rewrite repository docs and skill content in place so methodology remains intact, but persona- and account-bound language is removed or reduced to a short README attribution/migration note.

**Tech Stack:** Markdown, YAML frontmatter, Python, git, ripgrep

---

## File Structure Map

- Modify: `README.md` — neutralize top-level copy, rename skill table entry, add migration/attribution note, keep repo name unchanged in install examples only where necessary
- Modify: `CLAUDE.md` — convert from public mirror/publishing instructions into local maintenance guidance
- Modify: `hv-analysis/SKILL.md` — depersonalize frontmatter/body and update cross-skill references from `khazix-writer` to `longform-writer`
- Modify: `hv-analysis/scripts/md_to_pdf.py` — neutral default author
- Rename: `khazix-writer/` → `longform-writer/`
- Modify: `longform-writer/SKILL.md` — rename skill metadata/title and rewrite body from persona emulation to reusable long-form authorial-style writing guidance
- Modify: `longform-writer/references/content_methodology.md` — remove persona-bound references and keep method rules
- Modify: `longform-writer/references/style_examples.md` — replace identity-specific framing/examples with neutral style examples or distilled rules
- Modify: `prompts/橫縱分析法.md` — keep framework, remove founder attribution
- Modify: `docs/superpowers/specs/2026-04-23-repo-depersonalization-design.md` — update references from `khazix-writer` to `longform-writer` and note that repo name stays unchanged

---

### Task 1: Rename `khazix-writer` to `longform-writer`

**Files:**
- Modify: `README.md`
- Modify: `hv-analysis/SKILL.md`
- Modify: `docs/superpowers/specs/2026-04-23-repo-depersonalization-design.md`
- Rename: `khazix-writer/` → `longform-writer/`
- Modify: `longform-writer/SKILL.md`

- [ ] **Step 1: Verify the old path exists before renaming**

Run:

```bash
ls /Users/jwang/Documents/Workspace/khazix-skills/khazix-writer
```

Expected: shows `SKILL.md` and `references/`

- [ ] **Step 2: Rename the folder**

Run:

```bash
mv "/Users/jwang/Documents/Workspace/khazix-skills/khazix-writer" "/Users/jwang/Documents/Workspace/khazix-skills/longform-writer"
```

Expected: the old path disappears and `longform-writer/` exists

- [ ] **Step 3: Update `longform-writer/SKILL.md` frontmatter and heading**

Replace the opening block with:

```md
---
name: longform-writer
description: |
  用於需要根據素材、觀點與既定作者風格，產出可發布的長篇文章時。適用於公眾號文章、深度稿件、方法論文章、產品觀察、現象解讀與基於素材的擴寫。當使用者要求「寫文章」「寫稿子」「續寫」「擴寫」「按某種風格寫成長文」時觸發。不用於短內容、純標題生成或單句摘要。
---

# 長文寫作
```

- [ ] **Step 4: Replace repo references from `khazix-writer` to `longform-writer`**

Apply these exact replacements:

```md
README.md
- | [**khazix-writer**](./khazix-writer/) |
+ | [**longform-writer**](./longform-writer/) |

hv-analysis/SKILL.md
- 不要用於公眾號寫作（那個用khazix-writer）
+ 不要用於公眾號寫作（那個用longform-writer）
```

And update the spec file path references from `khazix-writer` to `longform-writer` so the design artifact matches the agreed naming.

- [ ] **Step 5: Verify the rename references are consistent**

Run:

```bash
cd /Users/jwang/Documents/Workspace/khazix-skills && rg -n "khazix-writer|longform-writer" README.md CLAUDE.md hv-analysis longform-writer docs/superpowers/specs
```

Expected:
- `longform-writer` appears in active docs and skill metadata
- `khazix-writer` appears only if intentionally preserved in migration notes

- [ ] **Step 6: Commit the rename slice**

Run:

```bash
cd /Users/jwang/Documents/Workspace/khazix-skills && git add README.md hv-analysis/SKILL.md longform-writer docs/superpowers/specs/2026-04-23-repo-depersonalization-design.md && git commit -m "refactor: rename khazix-writer skill to longform-writer"
```

Expected: one commit containing the path rename and linked reference updates

---

### Task 2: Rewrite repository docs while keeping repo name unchanged

**Files:**
- Modify: `README.md`
- Modify: `CLAUDE.md`

- [ ] **Step 1: Rewrite the README intro and skills table entry**

Replace these lines:

```md
- # Khazix Skills
- 數字生命卡茲克的 AI 工具箱。
- 這裡是我自己正在使用、並經過長期打磨的 Prompts 和 Skills，現在決定把它們完整地、一字不改地開源出來。
```

With:

```md
# Khazix Skills

以繁體中文整理的 AI prompts 與 agent skills 倉庫。

這裡收錄可重複使用的研究與寫作工作流，重點是方法本身，而不是作者人設。
```

Replace the skill row description with:

```md
| [**longform-writer**](./longform-writer/) | 長文寫作 Skill，聚焦長篇文章的選題判斷、素材消化、風格控制與四層自檢體系 | [公眾號文章](https://mp.weixin.qq.com/s/AtxGrii_K-nzkwUM9SNhEg) |
```

- [ ] **Step 2: Add a migration and attribution section to README**

Insert before `## License`:

```md
## Migration / Attribution

- `khazix-writer` 已重命名為 `longform-writer`
- 本倉庫保留部分公開方法論素材的整理痕跡，但 skill 主體已改為中性、可重用的寫法
- 若你曾用舊名稱引用此 skill，請改用 `longform-writer`
```

- [ ] **Step 3: Rewrite `CLAUDE.md` from public-mirror instructions to local maintenance rules**

Replace the opening section with:

```md
# khazix-skills

本倉庫用來維護繁體中文 prompts 與 skills 的可重用版本。

## 維護原則

- 優先保留方法論與可操作流程，不保留作者人格設定
- 新增或修改 skill 時，先確認內容可以脫離特定個人品牌獨立成立
- README 只保留必要的 migration / attribution，skill 主體避免作者敘事
```

Delete the entire `## 發布規範` section and the `### 帳號資訊` section.

- [ ] **Step 4: Verify repo docs no longer depend on Khazix account identity**

Run:

```bash
cd /Users/jwang/Documents/Workspace/khazix-skills && rg -n "KKKKhazix|ClawHub:|Tessl workspace:|數字生命卡茲克的 AI 工具箱|一字不改地開源" README.md CLAUDE.md
```

Expected: no matches

- [ ] **Step 5: Commit the repo-doc rewrite**

Run:

```bash
cd /Users/jwang/Documents/Workspace/khazix-skills && git add README.md CLAUDE.md && git commit -m "docs: depersonalize repository documentation"
```

Expected: one commit for README and CLAUDE cleanup

---

### Task 3: Depersonalize `hv-analysis` and the prompt while preserving the framework

**Files:**
- Modify: `hv-analysis/SKILL.md`
- Modify: `hv-analysis/scripts/md_to_pdf.py`
- Modify: `prompts/橫縱分析法.md`

- [ ] **Step 1: Rewrite `hv-analysis/SKILL.md` frontmatter description to remove author attribution**

Replace the opening description block with:

```md
---
name: hv-analysis
description: |
  用於需要對產品、公司、概念、技術或人物做系統性深度研究時。核心是雙軸分析：縱軸追蹤研究對象從誕生到當下的發展歷程，橫軸比較其在當前時間切面中的競爭格局、同類位置與差異，最後交匯出判斷。適用於深度研究、競品分析、產業理解與人物研究，不用於簡單名詞解釋、長文寫作或純摘要任務。
---
```

- [ ] **Step 2: Rewrite the method-source and style paragraphs in `hv-analysis/SKILL.md`**

Make these exact replacements:

```md
- > 橫縱分析法由數字生命卡茲克（Khazix）提出...
+ > 橫縱分析法是一種結合歷時分析與共時比較的通用研究框架。核心原則不變：縱向追時間深度，橫向追同期廣度，最終交匯出判斷。

- 寫作風格需要在「研究報告的嚴謹」和「卡茲克的可讀性」之間找到平衡點。
+ 寫作風格需要在「研究報告的嚴謹」與「敘事可讀性」之間找到平衡點。
```

Rename any subsection titled `從卡茲克文風中借鑑的核心元素` to `寫作風格借鑑的核心元素`, and remove direct persona mentions throughout that section.

- [ ] **Step 3: Change the default PDF author to a neutral value**

In `hv-analysis/scripts/md_to_pdf.py`, make these exact replacements:

```python
- def generate_pdf(..., meta_line="", author="數字生命卡茲克"):
+ def generate_pdf(..., meta_line="", author="作者未指定"):

- parser.add_argument("--author", default="數字生命卡茲克", help="作者名")
+ parser.add_argument("--author", default="作者未指定", help="作者名")
```

- [ ] **Step 4: Remove founder attribution from `prompts/橫縱分析法.md`**

Replace the final section:

```md
## 方法論溯源

橫縱分析法由數字生命卡茲克提出...
```

With:

```md
## 方法說明

橫縱分析法結合縱向發展史與橫向競爭格局分析，適合用來研究產品、公司、概念與人物。核心原則不變：縱向追時間深度，橫向追同期廣度，最終交匯出判斷。
```

- [ ] **Step 5: Verify `hv-analysis` no longer contains persona-bound references**

Run:

```bash
cd /Users/jwang/Documents/Workspace/khazix-skills && rg -n "數字生命卡茲克|Khazix|卡茲克" hv-analysis prompts/橫縱分析法.md
```

Expected: no matches, or only intentional migration notes outside active skill bodies

- [ ] **Step 6: Commit the analysis-skill cleanup**

Run:

```bash
cd /Users/jwang/Documents/Workspace/khazix-skills && git add hv-analysis prompts/橫縱分析法.md && git commit -m "docs: depersonalize hv-analysis materials"
```

Expected: one commit covering skill text, prompt text, and script default changes

---

### Task 4: Rewrite `longform-writer` into a reusable long-form writing skill

**Files:**
- Modify: `longform-writer/SKILL.md`
- Modify: `longform-writer/references/content_methodology.md`
- Modify: `longform-writer/references/style_examples.md`

- [ ] **Step 1: Replace persona framing at the top of `longform-writer/SKILL.md`**

Replace lines equivalent to the current intro with this content:

```md
# 長文寫作

這個 skill 用來協助產出可發布的長篇文章。重點不是模仿某個固定人格，而是把高辨識度長文常見的做法拆成可重用的寫作原則、協作邊界與自檢流程。

你要做的不是扮演某個作者，而是根據使用者提供的素材、觀點、情緒與目標讀者，寫出一篇有判斷、有敘事、有人味的長文。
```

- [ ] **Step 2: Rewrite the core values and style rules into neutral authorial principles**

Keep the structure, but replace persona-labeled rules with these principles:

```md
- 永遠對主題保持真誠好奇
- 優先講人話，避免官樣文章和生成式套話
- 明確區分第一手經歷、觀點判斷與資料補充
- 讓文章同時有資訊量、情緒張力與可讀性
- 先有真實感，再追求漂亮措辭
```

- [ ] **Step 3: Rewrite references to remove identity-specific imitation instructions**

Apply these rules to both reference files:

```md
- 把「卡茲克風格」改成「高辨識度長文風格」或更具體的風格名稱
- 把「卡茲克改的」改成「修改後版本」
- 把依附於某個帳號身份的敘述，改寫成可泛化的寫作原則
- 如果例子完全依賴個人身份背景，刪掉例子並補成規則說明
```

- [ ] **Step 4: Keep the four-layer review system, but rename it neutrally if needed**

If the file contains checks such as “只有卡茲克才會寫出來的角度”, replace them with:

```md
這篇文章是否有清晰、具辨識度、只有這位作者才寫得出的觀察角度？
```

Any sentence instructing the model to “想象卡茲克本人會怎麼說” should become:

```md
改寫成更接近作者真實說話方式、更具體、更不完美但更像真人的表達。
```

- [ ] **Step 5: Verify the renamed skill family is neutralized**

Run:

```bash
cd /Users/jwang/Documents/Workspace/khazix-skills && rg -n "Khazix|數字生命卡茲克|卡茲克" longform-writer
```

Expected: no matches

- [ ] **Step 6: Commit the long-form writing rewrite**

Run:

```bash
cd /Users/jwang/Documents/Workspace/khazix-skills && git add longform-writer && git commit -m "docs: turn longform-writer into a neutral writing skill"
```

Expected: one commit covering the skill body and references

---

### Task 5: Final consistency pass and verification

**Files:**
- Modify if needed: `README.md`
- Modify if needed: `CLAUDE.md`
- Modify if needed: `hv-analysis/**`
- Modify if needed: `longform-writer/**`
- Modify if needed: `prompts/橫縱分析法.md`
- Modify if needed: `docs/superpowers/specs/2026-04-23-repo-depersonalization-design.md`

- [ ] **Step 1: Run the final branding sweep**

Run:

```bash
cd /Users/jwang/Documents/Workspace/khazix-skills && rg -n "Khazix|數字生命卡茲克|KKKKhazix|卡茲克|jwcrystal" .
```

Expected:
- no matches in active skill bodies and primary docs
- any remaining match must be intentional and easy to explain

- [ ] **Step 2: Inspect git diff for accidental scope creep**

Run:

```bash
cd /Users/jwang/Documents/Workspace/khazix-skills && git diff -- README.md CLAUDE.md hv-analysis longform-writer prompts docs/superpowers/specs/2026-04-23-repo-depersonalization-design.md
```

Expected: only renaming, depersonalization, and migration-note changes appear

- [ ] **Step 3: Fix any leftover reference identified by the sweep**

If `rg` still finds brand-bound references in active docs/skills, remove them immediately before the final commit. Do not leave them for later.

- [ ] **Step 4: Create the final consolidation commit**

Run:

```bash
cd /Users/jwang/Documents/Workspace/khazix-skills && git add README.md CLAUDE.md hv-analysis longform-writer prompts docs/superpowers/specs/2026-04-23-repo-depersonalization-design.md && git commit -m "docs: depersonalize skill repository content"
```

Expected: final clean-up commit after the repo-wide verification pass

- [ ] **Step 5: Confirm clean working tree**

Run:

```bash
cd /Users/jwang/Documents/Workspace/khazix-skills && git status --short
```

Expected: no output
