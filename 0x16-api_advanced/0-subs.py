#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers """


import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit.
             Returns 0 if the subreddit doesn't exist.
    """
    headers = {'User-Agent': 'myUniBotAgent/0.2'}
    response = requests.get('https://www.reddit.com/r/{}/about.json'
                            .format(subreddit), headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
