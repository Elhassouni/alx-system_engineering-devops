#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    # Correct URL formatting using f-string
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Update User-Agent header, split across lines to comply with 79-char
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        )
    }
    # Make the request with the custom User-Agent
    response = requests.get(url, headers=headers, allow_redirects=False)
    # Check if the subreddit doesn't exist (404)
    if response.status_code == 404:
        return 0
    # Parse the response JSON and handle possible errors
    try:
        results = response.json().get("data", None)
        if results:
            return results.get("subscribers", 0)
        return 0
    except ValueError:
        # If the response can't be parsed as JSON, return 0
        return 0
