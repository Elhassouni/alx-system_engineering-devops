#!/usr/bin/python3
"""
Uses Reddit API to print the number of subscribers of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # More descriptive User-Agent as per Reddit API guidelines
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
        )
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    try:
        data = response.json().get("data", None)
        if data:
            return data.get("subscribers", 0)
        return 0
    except ValueError:
        # Handle case where response is not valid JSON
        return 0
