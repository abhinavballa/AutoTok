import requests
import json

SUBREDDIT = "AmITheAsshole"  # Change this to your desired subreddit
POST_LIMIT = 5
OUTPUT_FILE = "posts.json"

headers = {"User-Agent": "RedditScraper/0.1 by YourUsername"}
url = f"https://www.reddit.com/r/{SUBREDDIT}/new.json?limit={POST_LIMIT}"

response = requests.get(url, headers=headers)
response.raise_for_status()
data = response.json()

posts = []
for post in data["data"]["children"]:
    post_data = post["data"]
    posts.append({
        "title": post_data.get("title", ""),
        "author": post_data.get("author", ""),
        "selftext": post_data.get("selftext", ""),
        "url": f"https://reddit.com{post_data.get('permalink', '')}",
        "score": post_data.get("score", 0)
    })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print(f"Saved {len(posts)} posts to {OUTPUT_FILE}") 