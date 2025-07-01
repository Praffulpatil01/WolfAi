#import requests
#from bs4 import BeautifulSoup
#import random

#def fetch_trending_topic():
# print("🔍 Fetching trending topics from

from pytrends.request import TrendReq
import random


def fetch_trending_topic():
    print("🧠 Fetching trending topic with pytrends (real-time)...")
    try:
        pytrends = TrendReq(hl='en-IN', tz=330)
        df = pytrends.realtime_trending_searches(pn='IN')  # Works in 2025!

        topics = df['title'].tolist()
        print(f"🗞️ Got {len(topics)} real-time topics")

    except Exception as e:
        print("❌ pytrends fetch failed:", e)
        topics = ["Top AI Tools 2025", "How GPT-5 Works", "Future of AI"]

    ai_keywords = [
        "ai", "chatgpt", "openai", "gpt", "robot", "tech", "machine"
    ]
    filtered = [
        t for t in topics if any(kw in t.lower() for kw in ai_keywords)
    ]

    topic = random.choice(filtered if filtered else topics)
    print(f"📈 Selected topic: {topic}")
    return topic
