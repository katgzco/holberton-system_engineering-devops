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
    username = user.get("name")

    filename = "{}.json".format(sys.argv[1])

    with open(filename, mode='w') as file:
        for task in todo:
            json.dump({user_id: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }]}, file)
