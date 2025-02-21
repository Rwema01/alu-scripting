#!/usr/bin/python3
"""Script that fetches the top 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Return the titles of the top 10 hot posts from a given subreddit.
    
    If the subreddit is invalid or doesn't exist, print 'None'.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://reddit.com/r/{subreddit}.json"
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        children = json_data.get('data', {}).get('children', [])
        for i in range(min(10, len(children))):
            print(children[i].get('data', {}).get('title'))
    else:
        print(None)
