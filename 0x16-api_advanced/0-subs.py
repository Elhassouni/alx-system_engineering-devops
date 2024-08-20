#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subs for a subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
            "User-Agent": "v1.0.0"
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    res = response.json().get("data")
    return res.get("subscribers")
