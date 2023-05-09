#/usr/bin/python3

import requests

def recurse(subreddit, hot_list=[], last_post=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 100}
    if last_post:
        params['after'] = last_post
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 404:
        return None
    data = response.json()
    for post in data['data']['children']:
        hot_list.append(post['data']['title'])
    if data['data']['after'] is None:
        return hot_list
    return recurse(subreddit, hot_list, data['data']['after'])

