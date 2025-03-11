#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts from a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'myRedditBot/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None", end='')  # Avoid extra new line
        return

    try:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print("None", end='')  # Handle empty subreddit case
            return

        for post in posts:
            print(post['data']['title'].strip())  # Remove trailing spaces

    except Exception:
        print("None", end='')  # Handle unexpected errors
