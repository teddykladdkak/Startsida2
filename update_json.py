import feedparser
import json
from datetime import datetime

# RSS-flöden att hämta
feeds = [
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://hnrss.org/frontpage"
]

data = {
    "lastUpdated": datetime.utcnow().isoformat() + "Z",
    "feeds": []
}

for url in feeds:
    parsed = feedparser.parse(url)
    items = []
    for entry in parsed.entries[:5]:  # ta de 5 senaste
        items.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.get("published", "")
        })
    data["feeds"].append({
        "url": url,
        "items": items
    })

# Spara till JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
