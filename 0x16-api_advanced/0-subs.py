#!/usr/bin/python3
""" Script defines func that gets info of subreddit, returns amount of subs"""
import requests


def number_of_subscribers(subreddit):
    """ Function receives subreddit to look for as parameter"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 '
                  'Safari/537.36 OPR/85.0.4341.79')
    headers = {
        'User-Agent': user_agent
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    response.raise_for_status()
    if response.status_code != 200:
        return 0
    json_res = response.json()

    if 'data' not in json_res:
        return 0
    elif 'subscribers' not in json_res.get('data'):
        return 0
    else:
        return json_res['data']['subscribers']
