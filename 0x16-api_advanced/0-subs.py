#!/usr/bin/python3
"""a module that holds the definition for number_of_subscribers"""
from requests import get


def number_of_subscribers(subreddit):
    """a function that queries the Reddit API and returns
       the number of subscribers
    """
    res = get(f'https://www.reddit.com/r/{subreddit}/about.json')
    res = res.json()
    res = res.get('data').get('subscribers')

    if res is None:
        return 0

    return res
