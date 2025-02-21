#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:subreddit.top.ten:v1.0 (by /u/yourusername)'}
    params = {'limit': 10}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        
        if posts:
            for post in posts:
                print(post["data"].get("title"))
        else:
            print(None)
    else:
        print(None)
