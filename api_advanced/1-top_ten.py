#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Print the titles of the first 10 hot posts from a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyRedditBot/0.1"}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return
    
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    
    if not posts:
        print(None)
        return
    
    for post in posts:
        print(post["data"]["title"])
