#!/usr/bin/python3
"""
Export data in the JSON format.
"""
import json
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} USER_ID".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    response = requests.get(url)
    tasks = response.json()

    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    username = response.json().get('username')

    data = {user_id: []}
    for task in tasks:
        data[user_id].append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username
        })

    with open('{}.json'.format(user_id), 'w') as json_file:
        json.dump(data, json_file)
