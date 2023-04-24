#!/usr/bin/python3
"""Gets information about an employee's TODO list progress from the specified REST API."""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    url_users = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    response_users = requests.get(url_users)
    response_todos = requests.get(url_todos)

    if response_users.status_code != 200:
        print("User not found")
        sys.exit(1)

    employee_name = response_users.json().get("name")
    total_tasks = len(response_todos.json())
    done_tasks = [task for task in response_todos.json() if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
