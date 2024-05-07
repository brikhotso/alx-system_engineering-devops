#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the first 10 hot posts """


import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    headers = {'User-Agent': 'myUniBotAgent/0.2'}
    response = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                            .format(subreddit), headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            children = data.get('children')
            if children:
                for i, post in enumerate(children[:10]):
                    print("{}. {}".format(i+1, post.get('data').get('title')))
        else:
            print("None")
    else:
        print("None")
