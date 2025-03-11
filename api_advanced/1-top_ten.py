#!/usr/bin/python3
"""
Script that fetches and prints the titles of the first 10 hot posts from a given subreddit.
If the subreddit is invalid or contains no posts, it will return None.

Module uses the Reddit API to interact with subreddits and retrieve post data.
"""

import requests


def top_ten(subreddit):
    """Return the titles of the first 10 hot posts for the given subreddit.
    If the subreddit is invalid or has no posts, return None."""
    
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://reddit.com/r/{subreddit}/hot.json"
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])
        
        if posts:  # Check if there are posts
            for i in range(min(10, len(posts))):  # Ensure not to go beyond available posts
                print(posts[i]['data']['title'])
            print("OK")  # Print OK after displaying the posts
        else:
            print("None")  # If there are no posts, print None
    else:
        print("None")  # If the subreddit is invalid, print None

