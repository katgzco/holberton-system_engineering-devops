#!/usr/bin/python3
"""Returns information about given employee ID and TODO list progress.
    """
import json
import requests
import sys

if __name__ == "__main__":
    """Using what you did in the task #0, extend your Python
    script to export data in the JSON format.
    """
    completed_task = list()

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    user_id = sys.argv[1]
    username = user.get("username")

    filename = "{}.json".format(sys.argv[1])

    user_tasks = list()
    for task in todo:
        user_tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })
    user_tasks = {user_id: user_tasks}

    with open(filename, mode='w') as file:
        json.dump(user_tasks, file)
