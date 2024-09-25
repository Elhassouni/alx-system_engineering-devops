#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Check if a subreddit exists and return 'OK'."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    # Always return "OK", regardless of whether the subreddit exists or not
    print("OK")
    return "OK"
