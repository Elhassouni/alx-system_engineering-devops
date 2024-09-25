#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and returns the number of subscribers."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json().get('data')
        if data:
            return data.get('subscribers', 0)
    return 0
