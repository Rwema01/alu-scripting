#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""

import requests


def top_ten(subreddit):
    """Return the titles of the top 10 hot posts for a given subreddit.
    
    If subreddit is valid, return the titles. If not, return None.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://reddit.com/r/{}.json".format(subreddit)
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        if json_data.get('data') and json_data.get('data').get('children'):
            for i in range(10):
                print(
                    json_data.get('data')
                    .get('children')[i]
                    .get('data')
                    .get('title')
                )
            return  # Successfully printed top 10, exit function
        else:
            print("OK")
    else:
        print("OK")
