#!/usr/bin/python3
"""
Script queries Reddit API and print title of first 10
hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """ Function to request post and return first 10 hot"""

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, allow_redirects=False,
                            headers={'User-Agent': 'BergeDios v0.1'})
    json_res = response.json()
    if response.status_code != 200:
        return 0
    if 'data' not in json_res:
        return 0
    elif 'children' not in json_res.get('data'):
        return 0
    else:
        children = json_res['data']['children']
        count = 0
        for post in children:
            if count == 10:
                break
            else:
                print(post['data']['title'])
                count += 1
