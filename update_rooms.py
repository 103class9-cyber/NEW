import os
import requests
from bs4 import BeautifulSoup

# 設定
html_path = "index.html"
headers = {"User-Agent": "Mozilla/5.0"}
session = requests.Session()

print("☕ [系統觀測模式啟動] 自動上鎖邏輯已封印，僅記錄統計。")

# 讀取 index.html
with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# 觀測招待所
for link in soup.find_all("a", attrs={"data-room": True}):
    try:
        res = session.get(link["href"], headers=headers, timeout=10)
        # 模擬觀測行為
        print(f"房號 {link['data-room']} ｜ 觀測完畢")
    except: 
        print(f"⚠️ 房號 {link['data-room']} 連線異常")

print("✅ 觀測工作結束。")
