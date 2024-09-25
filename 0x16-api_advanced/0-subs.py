#!/usr/bin/python3
"""
Queries a Reddit API

IMPORTS: requests
requests: Send and receive data packets from a URI
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries a valid subreddit and retrives the no of subs

    Args:
    subreddit(str): A reddit topic

    Return:
    No of subs a subreddit has
    """
    try:
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        response = requests.get(url, allow_redirects=False)
    except Exception as e:
        print(f'An exception has occurred: {e}')
        return 0

    if response.status_code == 200:
        resp_json = response.json()
        no_subs = rsp_json['data']['subscribers']
        return no_subs
    elif response.status_code == 301:
        new_loc = response.headers['Location']

        try:
            new_resp = requests.get(new_loc)
        except Exception as e:
            print(f'An exception has occurred: {e}')
            return 0

        resp_json = new_resp.json()
        no_subs = resp_json['data']['subscribers']
        return no_subs

    else:
        return 0
