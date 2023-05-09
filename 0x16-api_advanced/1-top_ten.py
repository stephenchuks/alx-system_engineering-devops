#/usr/bin/python3

import requests

def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        print(None)
    else:
        data = response.json().get("data")
        children = data.get("children")
        for child in children:
            print(child.get("data").get("title"))

