#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def numberof_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/%7B%7D/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
