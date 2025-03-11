#!/usr/bin/python3
"""
Script that fetches and prints the titles of the first 10 hot posts from a given subreddit.
If the subreddit is invalid or contains no posts, it will return None.

Module uses the Reddit API to interact with subreddits and retrieve post data.
"""
import requests


def top_ten(subreddit):
    """Fetch and print titles of the first 10 hot posts from a given subreddit.
    If the subreddit is valid, print "OK". If the subreddit is invalid, print "None"."""

    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://reddit.com/r/{subreddit}.json"
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])
        
        if posts:  # Check if there are any posts
            for i in range(min(10, len(posts))):  # Ensure not to exceed available posts
                print(posts[i]['data']['title'])
            print("OK")  # Print OK after displaying posts
        else:
            print("None")  # If there are no posts in the subreddit
    else:
        print("None")  # If the subreddit is invalid, print None

