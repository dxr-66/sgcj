#!/usr/bin/env python3
"""从 articles.js 中提取文章数据并生成 rss.xml"""
import re
import html as html_mod
from datetime import datetime

with open("articles.js", "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r"var ARTICLES = \[(.*?)\];", content, re.DOTALL)
if not match:
    print("ERROR: 未找到 ARTICLES 数组")
    exit(1)

articles_str = match.group(1)
records = re.findall(
    r'\{\s*date:"([^"]+)",\s*title:"([^"]+)",\s*tags:\[(.*?)\],\s*excerpt:"([^"]+)",\s*url:"([^"]+)",\s*source:"([^"]+)"\s*\}',
    articles_str
)

SITE_TITLE = "拾光萃集"
SITE_DESC = "收集值得回看的文字 —— 人文、旅游、AI 与科技领域的有益知识。"
SITE_URL = "https://8000-74b80a2994b3e575.monkeycode-ai.online"

items = []
for date_str, title, tags_raw, excerpt, url, source in records:
    tags = [t.strip().strip('"') for t in tags_raw.split(",")]
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d")
        rfc_date = d.strftime("%a, %d %b %Y 08:00:00 +0800")
    except ValueError:
        rfc_date = date_str

    safe_title = html_mod.escape(title.strip())
    safe_excerpt = html_mod.escape(excerpt.strip())
    safe_source = html_mod.escape(source.strip())
    safe_tags = html_mod.escape(", ".join(tags))

    desc = f"<p>{safe_excerpt}</p><p>标签: {safe_tags} | 来源: {safe_source}</p>"
    if url and url != "#":
        desc += f'<p><a href="{html_mod.escape(url)}">阅读原文</a></p>'

    link = url if url and url != "#" else SITE_URL

    items.append(f"""    <item>
      <title>{safe_title}</title>
      <link>{html_mod.escape(link)}</link>
      <guid isPermaLink="false">{date_str}-{html_mod.escape(title.strip().replace(" ", "-"))}</guid>
      <description>{desc}</description>
      <pubDate>{rfc_date}</pubDate>
      <category>{safe_tags}</category>
    </item>""")

rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{SITE_TITLE}</title>
    <link>{SITE_URL}</link>
    <description>{SITE_DESC}</description>
    <language>zh-CN</language>
    <lastBuildDate>{datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0800")}</lastBuildDate>
    <atom:link href="{SITE_URL}/rss.xml" rel="self" type="application/rss+xml"/>
{chr(10).join(items)}
  </channel>
</rss>
"""

with open("rss.xml", "w", encoding="utf-8") as f:
    f.write(rss)

print(f"OK: 已生成 rss.xml ({len(records)} 篇文章)")
