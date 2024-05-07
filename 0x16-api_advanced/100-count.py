#!/usr/bin/python3
""" Contains count words function """


import requests


def fetch_titles(subreddit, after=None):
    """
    Fetch titles of hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        after (str): The "after" parameter for pagination.

    Returns:
        list or None: A list containing the titles of hot articles,
                      or None if no results are found.
    """
    headers = {'User-Agent': 'myUniBotAgent/0.2'}
    params = {'after': after} if after else {}
    response = requests.get('https://www.reddit.com/r/{}/hot.json'
                            .format(subreddit), headers=headers,
                            params=params)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            return [post['data']['title'] for post in data.get('children')]
    return None


def count_words(subreddit, word_list, counts=None):
    """
    Recursively count occurrences of keywords in hot articles.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count occurrences.
        counts (dict): A dictionary to store counts of each keyword.

    Returns:
        None
    """
    if counts is None:
        counts = {}

    titles = fetch_titles(subreddit)
    if titles:
        for title in titles:
            words = title.lower().split()
            words = [word.strip('.,?!:;') for word in words]
            for word in word_list:
                if word.lower() in words:
                    counts[word.lower()] = (counts.get(word.lower(), 0) +
                                            words.count(word.lower()))

        after = titles[-1] if titles else None
        count_words(subreddit, word_list, counts)

    if counts:
        sorted_counts = sorted(counts.items(),
                               key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
