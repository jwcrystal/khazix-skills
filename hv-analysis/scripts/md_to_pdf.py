#!/usr/bin/env python3
"""
橫縱分析法報告 Markdown → PDF 轉換腳本 (WeasyPrint版)
用法: python md_to_pdf.py input.md output.pdf [--title "報告標題"] [--author "作者"]

依賴: pip install weasyprint markdown --break-system-packages
"""

import sys
import os
import re
import argparse
import markdown

# ── CSS 樣式 ──
CSS_TEMPLATE = """
@page {
    size: A4;
    margin: 25mm 20mm 20mm 20mm;

    @top-center {
        content: "HEADER_TEXT";
        font-family: "PingFang TC", "Noto Sans TC", "Droid Sans Fallback", sans-serif;
        font-size: 8pt;
        color: #95a5a6;
        border-bottom: 0.5pt solid #ecf0f1;
        padding-bottom: 3mm;
    }

    @bottom-center {
        content: "第 " counter(page) " 頁";
        font-family: "PingFang TC", "Noto Sans TC", "Droid Sans Fallback", sans-serif;
        font-size: 8pt;
        color: #95a5a6;
        border-top: 0.8pt solid #1a5276;
        padding-top: 2mm;
    }
}

@page :first {
    @top-center { content: none; }
    @bottom-center { content: none; }
}

body {
    font-family: "PingFang TC", "Noto Sans TC", "Droid Sans Fallback", sans-serif;
    font-size: 10.5pt;
    line-height: 1.75;
    color: #2c3e50;
    text-align: justify;
}

/* 封面 */
.cover {
    page-break-after: always;
    text-align: center;
    padding-top: 45%;
}
.cover h1 {
    font-size: 28pt;
    color: #1a5276;
    margin-bottom: 8mm;
    font-weight: bold;
    letter-spacing: 2pt;
}
.cover .subtitle {
    font-size: 14pt;
    color: #95a5a6;
    margin-bottom: 6mm;
}
.cover .meta {
    font-size: 11pt;
    color: #95a5a6;
    margin-bottom: 4mm;
}
.cover .divider {
    width: 60%;
    margin: 8mm auto;
    border: none;
    border-top: 1.5pt solid #1a5276;
}

/* 一級標題 */
h1 {
    font-size: 20pt;
    color: #1a5276;
    margin-top: 16mm;
    margin-bottom: 6mm;
    padding-bottom: 3mm;
    border-bottom: 2pt solid #1a5276;
    page-break-before: always;
    font-weight: bold;
}

/* 二級標題 */
h2 {
    font-size: 14pt;
    color: #1e8449;
    margin-top: 10mm;
    margin-bottom: 5mm;
    font-weight: bold;
}

/* 三級標題 */
h3 {
    font-size: 12pt;
    color: #2e86c1;
    margin-top: 6mm;
    margin-bottom: 3mm;
    font-weight: bold;
}

h4 {
    font-size: 11pt;
    color: #5b2c6f;
    margin-top: 5mm;
    margin-bottom: 2mm;
    font-weight: bold;
}

/* 段落 */
p {
    margin-top: 1.5mm;
    margin-bottom: 1.5mm;
    orphans: 3;
    widows: 3;
}

/* 引用塊 */
blockquote {
    margin: 4mm 0;
    padding: 4mm 4mm 4mm 10mm;
    background: #f8f9fa;
    border-left: 3pt solid #1a5276;
    color: #5d6d7e;
    font-size: 10pt;
}
blockquote p {
    margin: 1mm 0;
}

/* 粗體 */
strong, b {
    font-weight: bold;
    color: #1a252f;
}

/* 行內程式碼 */
code {
    font-family: "Courier New", Courier, monospace;
    background: #fdf2e9;
    color: #c0392b;
    padding: 0.5mm 1.5mm;
    border-radius: 2pt;
    font-size: 9.5pt;
}

/* 表格 */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 4mm 0;
    font-size: 9.5pt;
}
thead th {
    background: #1a5276;
    color: white;
    padding: 3mm;
    text-align: left;
    font-weight: bold;
}
tbody td {
    padding: 2.5mm 3mm;
    border-bottom: 0.5pt solid #bdc3c7;
}
tbody tr:nth-child(even) {
    background: #f8f9fa;
}

/* 分隔線 */
hr {
    border: none;
    border-top: 0.5pt solid #bdc3c7;
    margin: 4mm 0;
}

/* 列表 */
ul, ol {
    margin: 2mm 0;
    padding-left: 8mm;
}
li {
    margin-bottom: 1mm;
}

/* 連結 */
a {
    color: #2e86c1;
    text-decoration: none;
}
"""


def md_to_html(md_text, title="橫縱分析報告", subtitle="橫縱分析法深度研究報告",
               meta_line="", author="Jared Wang"):
    """將 Markdown 轉為帶封面的 HTML"""

    # 用 markdown 庫轉換正文
    html_body = markdown.markdown(
        md_text,
        extensions=['tables', 'fenced_code', 'nl2br'],
        output_format='html5'
    )

    # 移除正文中的第一個 h1（會用在封面上）
    first_h1_match = re.search(r'<h1>(.*?)</h1>', html_body)
    if first_h1_match:
        extracted_title = first_h1_match.group(1)
        if not title or title == "橫縱分析報告":
            title = extracted_title
        html_body = html_body.replace(first_h1_match.group(0), '', 1)

    # 替換 CSS 中的頁首佔位符
    css = CSS_TEMPLATE.replace("HEADER_TEXT", f"{title}  |  橫縱分析法深度研究報告")

    # 構建封面
    cover_html = f"""
    <div class="cover">
        <h1 style="page-break-before: avoid; border: none;">{title}</h1>
        <div class="subtitle">{subtitle}</div>
        {"<div class='meta'>" + meta_line + "</div>" if meta_line else ""}
        <hr class="divider">
        <div class="meta">作者: {author}</div>
    </div>
    """

    full_html = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <style>{css}</style>
</head>
<body>
{cover_html}
{html_body}
</body>
</html>"""

    return full_html


def main():
    parser = argparse.ArgumentParser(description="橫縱分析法報告 Markdown → PDF")
    parser.add_argument("input", help="輸入的 Markdown 檔案路徑")
    parser.add_argument("output", help="輸出的 PDF 檔案路徑")
    parser.add_argument("--title", default=None, help="報告標題")
    parser.add_argument("--author", default="Jared Wang", help="作者名")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        md_text = f.read()

    # 提取元資訊
    meta_line = ""
    for line in md_text.split("\n"):
        stripped = line.strip().lstrip(">").strip()
        if "研究時間" in stripped or "所屬領域" in stripped or "研究對象類型" in stripped:
            meta_line = stripped
            break

    html = md_to_html(md_text, title=args.title or "橫縱分析報告", meta_line=meta_line, author=args.author)

    # 儲存中間 HTML（便於除錯）
    html_path = args.output.replace('.pdf', '.html')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"[OK] HTML 已生成: {html_path}")

    # 轉 PDF
    from weasyprint import HTML
    HTML(string=html).write_pdf(args.output)
    size_kb = os.path.getsize(args.output) / 1024
    print(f"[OK] PDF 已生成: {args.output} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
