#!/usr/bin/python3
"""retrieves the list of all reddit subscribers"""
from requests import get


def num_of_subs(subreddit):
    """retrives the number of subscribers for a subredit"""
    header = {"User-Agent": 'Google Chrome Version 81.0.4044.129'}
    respon = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
              headers=header, allow_redirects=False)
    code = respon.status_code
    return 0 if code == 404 else respon.json().get("data").get("subscribers")
