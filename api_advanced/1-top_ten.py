#!/usr/bin/python3
"""
Module to query the Reddit API and print the titles of the first 10 hot posts
for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            print("None")  # If subreddit is invalid, print "None"
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print("None")  # No posts available
            return

        for post in posts:
            print(post['data']['title'])

    except requests.RequestException:
        print("None")  # Handle request failures


if __name__ == "__main__":
    top_ten("programming")

