import feedparser
import json
from datetime import datetime
from bs4 import BeautifulSoup

def strip_html(text):
    if not text:
        return ""
    return BeautifulSoup(text, "html.parser").get_text()

# RSS-flöden att hämta
feeds = [
    {"link": "https://skaneskommuner.se/news/feed/atom/", "amount": 2},
    {"link": "http://svt.se/nyheter/rss.xml", "amount": 5},
    {"link": "http://svt.se/nyheter/regionalt/sydnytt/rss.xml", "amount": 4},
    {"link": "https://rss.aftonbladet.se/rss2/small/pages/sections/senastenytt/", "amount": 3},
    {"link": "https://feeds.expressen.se/nyheter/", "amount": 3}
]

data = {
    "lastUpdated": datetime.utcnow().isoformat() + "Z",
    "feeds": []
}

for url in feeds:
    parsed = feedparser.parse(url["link"])
    items = []
    for entry in parsed.entries[:url["amount"]]:  # ta de 5 senaste
        items.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.get("published", ""),
            "description": strip_html(entry.description)
        })
    data["feeds"].append({
        "url": url,
        "items": items
    })

# Spara till JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)








