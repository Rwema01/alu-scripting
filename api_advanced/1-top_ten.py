#!/usr/bin/python3
"""
Reddit API script to fetch the top 10 hot posts from a given subreddit.

Usage:
    Call the function `top_ten(subreddit)` with the name of a subreddit
    to print the titles of the top 10 hot posts.
"""

import requests


def top_ten(subreddit):
    """
    Prints the top 10 hot post titles of a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None: Prints the post titles or 'None' if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyAPI/0.0.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    json_data = response.json()
    posts = json_data.get("data", {}).get("children", [])

    if not posts:
        print(None)
        return

    for post in posts[:10]:  # Ensure we only print up to 10 posts
        print(post["data"].get("title", "None"))
