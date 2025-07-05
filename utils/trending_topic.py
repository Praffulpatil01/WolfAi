import feedparser
import random


def fetch_trending_topic():
    print("🧠 Fetching trending topic from Google News RSS (AI)...")
    try:
        url = "https://news.google.com/rss/search?q=artificial+intelligence"
        feed = feedparser.parse(url)
        topics = [entry.title for entry in feed.entries]

        if not topics:
            raise ValueError("No topics found in RSS feed.")

        print(f"🗞️ Got {len(topics)} AI-related news headlines")

    except Exception as e:
        print("❌ RSS fetch failed:", e)
        topics = [
            "Top AI Tools 2025", "How GPT-5 Works",
            "Future of AI in Agriculture", "AI vs Human Creativity",
            "Rise of Autonomous Drones", "Open Source LLMs"
        ]
        print("🛟 Using fallback static topics")

    ai_keywords = [
        "ai", "chatgpt", "openai", "gpt", "robot", "tech", "machine"
    ]
    filtered = [
        t for t in topics if any(kw in t.lower() for kw in ai_keywords)
    ]

    topic = random.choice(filtered if filtered else topics)
    print(f"📈 Selected topic: {topic}")
    return topic
