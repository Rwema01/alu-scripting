#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""

import requests


def top_ten(subreddit):
    """Return the titles of the top 10 hot posts for a given subreddit.
    
    If subreddit is valid, return the titles. If not, return None.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(
        subreddit)
    response = requests.get(subreddit_url, headers=headers, allow_redirects=False)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        json_data = response.json()
        # Ensure the JSON data contains the expected structure
        if 'data' in json_data and 'children' in json_data['data']:
            for post in json_data['data']['children']:
                print(post['data']['title'])
        else:
            print(None)
    else:
        print(None)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
