#!/usr/bin/python3
"""a module that holds the definition for number_of_subscribers"""
from requests import get


def number_of_subscribers(subreddit):
    """a function that queries the Reddit API and returns
       the number of subscribers
    """
    user_agent = {'User-Agent': 'Google Chrome Version 81.0.4044.1    29'}
    try:
        res = get(f'https://www.reddit.com/r/{subreddit}/about.json',
                  headers=user_agent)
        if res.status_code != 200:
            return 0

        data = res.json().get('data')
        if data is None:
            return 0

        subscribers = data.get('subscribers')
        return subscribers if subscribers is not None else 0

    except Exception as e:
        return 0
