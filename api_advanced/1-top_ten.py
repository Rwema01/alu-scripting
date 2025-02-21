#!/usr/bin/python3
"""
1-top_ten
Queries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit.
If the subreddit is invalid, prints None.
"""
import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            posts = response.json()['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except Exception:
        print(None)
