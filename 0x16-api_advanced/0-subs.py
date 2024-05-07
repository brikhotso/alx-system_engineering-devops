#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ return number of subsbribers """
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers)

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
