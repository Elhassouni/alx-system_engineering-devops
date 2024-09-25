#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot
   posts for a given subreddit"""


import requests


def top_ten(subreddit):
    """Prints the titles"""

    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9"
    # made limit 9 since index is 0 - 9 gives 10 posts
    headers = {'User-Agent': 'custom-script/1.0'}

    try:
        response = requests.get(base_url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)