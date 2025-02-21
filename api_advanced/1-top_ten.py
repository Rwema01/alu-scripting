#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts of a given subreddit.
"""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/fake_user)"}  # Use a proper User-Agent
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {})
        posts = data.get("children", [])

        for post in posts:
            print(post["data"]["title"])
    else:
        print(None)
