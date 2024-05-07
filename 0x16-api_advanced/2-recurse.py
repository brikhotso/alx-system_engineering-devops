#!/usr/bin/python3
"""
    contain recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles
"""


import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively fetch the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles.

    Returns:
        list or None: A list containing the titles of all hot articles,
                      or None if no results are found.
    """
    headers = {'User-Agent': 'myUniBotAgent/0.2'}
    response = requests.get('https://www.reddit.com/r/{}/hot.json'
                            .format(subreddit),
                            headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            children = data.get('children')
            if children:
                for post in children:
                    hot_list.append(post.get('data').get('title'))

            after = data.get('after')
            if after:
                return recurse(subreddit, hot_list=hot_list)
            return hot_list
        else:
            return None
    else:
        return None
