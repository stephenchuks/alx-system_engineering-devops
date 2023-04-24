#!/usr/bin/python3
"""Gather data from an API"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            user_id)).json()

    completed_tasks = []
    for task in tasks:
        if task.get('completed'):
            completed_tasks.append(task)

    with open('{}.csv'.format(user_id), mode='w') as file:
        writer = csv.writer(
            file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow([user_id, user.get('username'), task.get(
                'completed'), task.get('title')])
