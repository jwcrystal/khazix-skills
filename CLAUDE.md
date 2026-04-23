# khazix-skills

通用 AI 工具箱倉庫，包含經過驗證的 Prompts 和 Skills。

> 原始來源：基於 [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) 的開源作品進行通用化改造。

## 開發工作區建議

- 建議維護一個開發工作區（例如 `skill-build/`），用於評估、測試、迭代
- 本倉庫作為對外成品，只放已穩定、準備公開的內容
- 新 skill **先在開發工作區跑通**，再把原始檔複製過來打包發布

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

1. 在開發工作區完成評估並確認穩定後，複製原始檔（`SKILL.md` + `scripts/` + `references/`）到本倉庫 `<skill-name>/`
2. 更新 `README.md` 對應表格，加上一行說明
3. 按下方「發布規範」同步三個平台
4. GitHub Release 打 tag，附上 `.skill` 包

## 發布規範

每次新增或更新 Skill / Prompt 後，必須同步發布到以下平台先占位，避免被他人 fork 搶註：

| 優先級 | 平台 | 操作 |
|--------|------|------|
| 1 | **ClawHub** (clawhub.ai) | `clawhub publish <path> --slug <name>` |
| 2 | **Tessl** (tessl.io) | `tessl skill publish --workspace <你的workspace> --public --skip-evals <path>` |
| 3 | **claude-skill-registry** | 向 `majiayu000/claude-skill-registry-core` 提 PR |

### 注意事項

- 不需要等使用者要求，有新 skill 就主動發布
- ClawHub 有 8192 token embedding 限制，若 SKILL.md 超限，先用精簡版占 slug，後續再用 `--version` 遞增更新完整版
- 精簡版必須保留方法論核心內容，不能只寫一句話占位
- 發布完成後，向使用者確認各平台狀態

### 帳號資訊（示例，請替換為你自己的）

- ClawHub: @你的用戶名
- Tessl workspace: 你的工作空間名稱
- GitHub: 你的用戶名/你的倉庫名
