# khazix-skills（github-share）

對外開源倉庫。把我在 `skill-build/` 裡打磨穩定的 Prompts 和 Skills，一字不改地鏡像出來給別人重複使用。GitHub: `KKKKhazix/khazix-skills`。

## 和 skill-build 的關係

- `my/skill-build/` — 開發工作區，評估、測試、迭代都在那邊
- `my/github-share/` — 對外成品鏡像，只放已穩定、準備公開的內容
- 新 skill **先在 skill-build 跑通**，再把原始檔複製過來打包發布

不要反過來做：不要在 github-share 裡直接開發，改動很容易失去評估上下文。

## 目錄結構

```
prompts/             單個 .md 檔，複製貼上即可使用的 Prompt
<skill-name>/        每個 Skill 一個資料夾，遵循 Agent Skills 標準
  SKILL.md             必填
  scripts/             可選，執行時腳本
  references/          可選，風格指南 / 示例庫
LICENSE              MIT
README.md            對外說明（繁體中文）
TERMINOLOGY.md       倉庫用詞統一規範
```

根目錄不要放零散檔案。

## 繁體中文與用詞規範

- 本倉庫預設使用 **繁體中文**，用語以 **台灣常用寫法** 為主
- 平台專名與既有品牌名稱保留原名，例如：公眾號、小紅書、知乎、飛書
- 新增或修改文件時，請以 [`TERMINOLOGY.md`](./TERMINOLOGY.md) 作為正式規範來源
- 若規範與外部介面、slug、skill name、frontmatter 或程式相容性衝突，**以相容性優先**

## 新增 Skill / Prompt 的動作順序

1. 在 skill-build 裡完成評估並確認穩定後，複製原始檔（`SKILL.md` + `scripts/` + `references/`）到本倉庫 `<skill-name>/`
2. 更新 `README.md` 對應表格，加上一行說明
3. 按下方「發布規範」同步三個平台
4. GitHub Release 打 tag，附上 `.skill` 包（來自 `skill-build/builds/`）

## 發布規範

每次新增或更新 Skill / Prompt 後，必須同步發布到以下平台先占位，避免被他人 fork 搶註：

| 優先級 | 平台 | 操作 |
|--------|------|------|
| 1 | **ClawHub** (clawhub.ai) | `clawhub publish <path> --slug <name>` |
| 2 | **Tessl** (tessl.io) | `tessl skill publish --workspace khazix-skills --public --skip-evals <path>` |
| 3 | **claude-skill-registry** | 向 `majiayu000/claude-skill-registry-core` 提 PR |

### 注意事項

- 不需要等使用者要求，有新 skill 就主動發布
- ClawHub 有 8192 token embedding 限制，若 SKILL.md 超限，先用精簡版占 slug，後續再用 `--version` 遞增更新完整版
- 精簡版必須保留方法論核心內容，不能只寫一句話占位
- 發布完成後，向使用者確認各平台狀態

### 帳號資訊

- ClawHub: @KKKKhazix
- Tessl workspace: khazix-skills
- GitHub: KKKKhazix/khazix-skills
