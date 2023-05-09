#!/usr/bin/python3

"""
titles of the top ten subreddits titles of the top ten subreddits
"""

from requests import get


def top_ten(subreddit):
    """
    return top 10 hot subredits return top 10 hot subredits
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    p = {'limit': 10}
    u = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    re = get(url, headers=user_agent, params=params)
    res = re.json()

    try:
        md = res.get('data').get('children')

        for i in md:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
