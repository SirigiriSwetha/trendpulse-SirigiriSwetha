import requests
import json
from datetime import datetime
import os

# 1. Define categories
categories = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "PGA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}

collected_stories = []
counts = {cat: 0 for cat in categories}

def fetch_data():
    try:
        print("Connecting to Hacker News... (checking internet)")
        # Added timeout=10 to prevent waiting forever
        response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json", timeout=10)
        top_ids = response.json()
        
        for story_id in top_ids:
            if all(count >= 20 for count in counts.values()):
                break
                
            item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            story = requests.get(item_url, timeout=10).json()
            
            if story and 'title' in story:
                title_lower = story['title'].lower()
                for cat, keywords in categories.items():
                    if counts[cat] < 20 and any(word.lower() in title_lower for word in keywords):
                        data = {
                            "post_id": story.get("id"),
                            "title": story.get("title"),
                            "category": cat,
                            "score": story.get("score"),
                            "num_comments": story.get("descendants", 0),
                            "author": story.get("by"),
                            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        collected_stories.append(data)
                        counts[cat] += 1
                        break

         # 1. Ensure the 'data' directory exists
        folder_name = "data"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # 2. Define the full path
        file_path = os.path.join(folder_name, "trends_20260414.json")

        # 3. Save the file
        with open(file_path, "w") as f:
            json.dump(collected_stories, f, indent=4)
            
        print(f"Success! Data saved to {file_path}")

    except requests.exceptions.ConnectionError:
        print("Error: No internet or site is blocked. Check your Wi-Fi or VPN.")
    except requests.exceptions.Timeout:
        print("Error: The request took too long. The site might be slow.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

fetch_data()