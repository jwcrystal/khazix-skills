# Khazix Skills

數字生命卡茲克的 AI 工具箱。

這裡是我自己正在使用、並經過長期打磨的 Prompts 和 Skills，現在決定把它們完整地、一字不改地開源出來。

兩種東西，一個目的，把我累積的方法論變成可重複使用的工具。

- **Prompts** — 輕量級，複製貼上到任何 AI 對話或 Deep Research 裡就能用
- **Skills** — 重量級，遵循 [Agent Skills](https://agentskills.io) 開放標準的結構化指令集，安裝後 Agent 會自動載入

> 本倉庫的繁體中文與台灣用語規範，見 [`TERMINOLOGY.md`](./TERMINOLOGY.md)。

## Prompts

| Prompt | 說明 | 用法 | 講解 |
|--------|------|------|------|
| [**橫縱分析法**](./prompts/橫縱分析法.md) | 通用深度研究框架，融合歷時—共時分析與競爭戰略視角，半小時產出一份萬字級研究報告 | 複製 Prompt，修改「研究對象」，丟進任何支援 Deep Research 的模型 | [公眾號文章](https://mp.weixin.qq.com/s/Y_uRMYBmdLWUPnz_ac7jWA) |

## Skills

| Skill | 說明 | 講解 |
|-------|------|------|
| [**hv-analysis**](./hv-analysis/) | 橫縱分析法深度研究 Skill，會自動連網收集資訊，縱向追時間深度、橫向追競爭廣度，最終輸出排版精美的 PDF 研究報告 | [公眾號文章](https://mp.weixin.qq.com/s/Y_uRMYBmdLWUPnz_ac7jWA) |
| [**khazix-writer**](./khazix-writer/) | 卡茲克公眾號長文寫作 Skill，包含完整的寫作風格規則、四層自檢體系、內容方法論與風格示例庫 | [公眾號文章](https://mp.weixin.qq.com/s/AtxGrii_K-nzkwUM9SNhEg) |

### Skill 安裝方式

**透過 Agent 安裝**

在 Claude Code、Codex、OpenClaw 等支援 Skill 的 Agent 中，直接對話：

```
安裝這個 skill：https://github.com/KKKKhazix/khazix-skills
```

**手動安裝**

1. 到本倉庫的 [Releases](https://github.com/KKKKhazix/khazix-skills/releases) 頁面下載對應 Skill 的 `.skill` 安裝包
2. 將 `.skill` 檔拖到對應工具的 Skills 目錄下

各工具的 Skills 安裝路徑：

| 工具 | 路徑 |
|------|------|
| Claude Code | `~/.claude/skills/` |
| OpenClaw | `~/.openclaw/skills/` |
| Codex | `~/.agents/skills/` |

## License

[MIT](./LICENSE)
