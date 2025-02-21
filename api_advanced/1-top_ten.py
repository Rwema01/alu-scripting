#!/usr/bin/python3
"""
1-top_ten: Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.

Requirements:
- Prints the first 10 hot post titles if the subreddit exists.
- Prints None if the subreddit does not exist.
- Does not follow redirects.
- Uses a proper User-Agent to avoid request blocking.
- Adheres to PEP8 style guide.
"""

import json
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
        try:
            data = response.json()
            posts = data.get("data", {}).get("children", [])
            if not posts:
                print(None)
            else:
                for post in posts:
                    print(post.get("data", {}).get("title"))
        except (json.JSONDecodeError, KeyError):
            print(None)
    else:
        print(None)
