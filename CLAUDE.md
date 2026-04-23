# khazix-skills

本倉庫用來維護繁體中文 prompts 與 skills 的可重用版本。

## 維護原則

- 優先保留方法論與可操作流程，不保留作者人格設定
- 新增或修改 skill 時，先確認內容可以脫離特定個人品牌獨立成立
- README 只保留必要的 migration / attribution，skill 主體避免作者敘事

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

## 修改順序

1. 先確認方法、觸發條件與輸出格式是否仍然成立
2. 若涉及人設或品牌綁定，優先改成中性可重用寫法
3. 更新 `README.md` 中對應的說明與 migration note
4. 最後再做 repo-wide 搜尋，確認沒有殘留品牌化描述
