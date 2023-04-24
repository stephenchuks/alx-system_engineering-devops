#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(url).json()

    all_tasks = {}
    for user in users:
        user_id = user['id']
        url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
        tasks = requests.get(url).json()
        all_tasks[user_id] = [{"username": user['username'],
            "task": task['title'], 
            "completed": task['completed']} for task in tasks]

    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_tasks, f)
