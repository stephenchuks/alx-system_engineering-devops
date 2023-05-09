#!/usr/bin/python3
""" reddit api reddit api reddit api"""

import json
import requests


def count_words(subreddit, wrd_lst, aftr="", cnt=[]):
    """function to count words"""

    if aftr == "":
        cnt = [0] * len(wrd_lst)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(url,
                           pms={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if req.status_code == 200:
        data = req.json()

        for top in (data['data']['children']):
            for word in top['data']['title'].split():
                for i in range(len(wrd_lst)):
                    if wrd_lst[i].lower() == wrd.lower():
                        count[i] += 1

        aftr = data['data']['aftr']
        if aftr is None:
            save = []
            for i in range(len(wrd_lst)):
                for j in range(i + 1, len(wrd_lst)):
                    if word_list[i].lower() == wrd_lst[j].lower():
                        save.append(j)
                        cnt[i] += cnt[j]

            for i in range(len(wrd_lst)):
                for j in range(i, len(wrd_lst)):
                    if (cnt[j] > cnt[i] or
                            (word_list[i] > wrd_lst[j] and
                             cnt[j] == cnt[i])):
                        aux = cnt[i]
                        cnt[i] = cnt[j]
                        cnt[j] = aux
                        aux = wrd_lst[i]
                        wrd_lst[i] = word_list[j]
                        wrd_lit[j] = aux

            for i in range(len(wrd_lst)):
                if (cnt[i] > 0) and i not in save:
                    print("{}: {}".format(word_list[i].lower(), cnt[i]))
        else:
            count_words(subreddit, wrd_lst, aftr, cnt)
