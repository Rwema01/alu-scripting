#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit."""
    base_url = 'https://www.reddit.com'
    api_uri = '{base}/r/{subreddit}/hot.json'.format(base=base_url, subreddit=subreddit)

    # Set a User-Agent
    user_agent = {'User-Agent': 'Python/requests'}

    # Set the Query Strings to Request
    payload = {'limit': 10}

    # Get the Response from Reddit API
    try:
        res = requests.get(api_uri, headers=user_agent, params=payload, allow_redirects=False)
        
        # Check if subreddit is invalid
        if res.status_code != 200:
            print("None")
            return

        # Attempt to parse JSON response
        try:
            res_json = res.json()
        except ValueError:
            print("None")
            return

        # Check if the response contains expected data
        if res_json.get('data') and res_json.get('data').get('children'):
            for post in res_json.get('data').get('children'):
                print(post.get('data', {}).get('title', "None"))
        else:
            print("None")

    except requests.RequestException:
        print("None")
