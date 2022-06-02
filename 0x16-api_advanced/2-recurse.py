#!/usr/bin/python3
"""
Script queries Reddit API recursively and save to list
title of hot posts for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Function to request post and returns list of hot articles"""

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, allow_redirects=False,
                            headers={'User-Agent': 'BergeDios v0.1'},
                            params={'after': after})
    json_res = response.json()
    if response.status_code != 200:
        return 0
    if 'data' not in json_res:
        return 0
    elif 'children' not in json_res.get('data'):
        return 0
    else:
        children = json_res['data']['children']
        for post in children:
            hot_list.append(post['data']['title'])
        after = json_res['data'].get('after')
        if not after:
            print(len(hot_list))
            return hot_list
        else:
             return recurse(subreddit, hot_list=hot_list, after=after)
