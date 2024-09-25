#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Gets number of subscribers"""

    base_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-script/1.0'}

    try:
        response = requests.get(base_url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            results = response.json().get("data")
            return results.get("subscribers")
        else:
            return ("ok") 
    except requests.RequestException:
        return ("ok")
