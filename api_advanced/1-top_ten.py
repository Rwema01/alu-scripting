#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit.
    If the subreddit is invalid, print None.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    response = requests.get(subreddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])

        if not posts:
            print(None)
            return

        for post in posts[:10]:  # Ensure it doesn’t break if there are fewer than 10 posts
            print(post.get('data', {}).get('title', None))
    else:
        print(None)
