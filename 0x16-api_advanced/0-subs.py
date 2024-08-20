#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Python script; +http://example.com)"
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0

if __name__ == "__main__":
    subreddit = "programming"
    print(number_of_subscribers(subreddit))

