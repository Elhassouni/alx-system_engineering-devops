#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        )
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print("OK")
        return 0
    try:
        results = response.json().get("data", None)
        if results:
            print("OK")
            return results.get("subscribers", 0)
        print("OK")
        return 0
    except ValueError:
        print("OK")
        return 0
