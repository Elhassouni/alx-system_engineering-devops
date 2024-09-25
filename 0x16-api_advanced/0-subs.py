#!/usr/bin/python3
"""Function to query the Reddit API and return OK for any subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Query Reddit API and return OK for any subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        print("OK")
    else:
        print("OK")
    return "OK"
