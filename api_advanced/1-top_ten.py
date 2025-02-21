#!/usr/bin/python3
"""
1-top_ten: Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:top_ten:v1.0 (by /u/yourusername)"}
    params = {"limit": 10}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print(None)
