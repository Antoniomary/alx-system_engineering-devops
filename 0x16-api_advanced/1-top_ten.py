#!/usr/bin/python3
"""a module that holds the definition for number_of_subscribers"""
from requests import get


def top_ten(subreddit):
    """a function that queries the Reddit API and
       prints the titles of the first 10 hot posts
       listed for a given subreddit
    """
    user_agent = {'User-Agent': 'Google Chrome Version 81.0.4044.1    29'}
    param = {'limit': 9}
    try:
        res = get(f'https://www.reddit.com/r/{subreddit}/hot.json',
                  headers=user_agent, params=param, allow_redirects=False)
        if res.status_code != 200:
            return print('None')

        data = res.json().get('data')
        if data is None:
            return print('None')

        children = data.get('children')
        if children is None:
            return print('None')

        for child in children:
            print(child.get('data').get('title'))

    except Exception as e:
        print('None')
