import requests
import time

response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
topstories_data = response.json()

for id in topstories_data[:30]:
    response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json")
    top_30_data = response.json()
    if top_30_data.get("title") and top_30_data.get("url"):
        print({"title": top_30_data["title"], "link": top_30_data["url"]})
    else:
        print({"title": top_30_data["title"], "link": None})
    time.sleep(1)
