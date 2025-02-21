#!/usr/bin/python3
"""
Reddit API Query Script

This module defines a function to fetch and print the titles of the first
10 hot posts from a given subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    If the subreddit is invalid or inaccessible, prints "None".
    """
    base_url = "https://www.reddit.com"
    api_uri = f"{base_url}/r/{subreddit}/hot.json"

    # Set a User-Agent
    user_agent = {"User-Agent": "Python/requests"}

    # Set the Query Strings to Request
    payload = {"limit": 10}

    try:
        res = requests.get(
            api_uri, headers=user_agent, params=payload, allow_redirects=False
        )

        # Check if subreddit is invalid or inaccessible
        if res.status_code != 200:
            print("None")
            return

        # Attempt to parse JSON response
        try:
            res_json = res.json()
        except ValueError:
            print("None")
            return

        # Check if response contains expected data
        posts = res_json.get("data", {}).get("children", [])

        if not posts:
            print("None")
            return

        # Print the titles of the 10 hot posts
        for post in posts:
            print(post.get("data", {}).get("title", "None"))

    except requests.RequestException:
        print("None")
