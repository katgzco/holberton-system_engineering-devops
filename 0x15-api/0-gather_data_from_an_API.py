#!/usr/bin/python3
"""Returns information about given employee ID and TODO list progress.
    """

import requests
import sys

if __name__ == "__main__":

    completed_task = list()

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    for task in todo:
        if (task.get("completed") is True):
            completed_task.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(user.get("name"), len(completed_task), len(todo)))

    for task in completed_task:
        print('\t' + task)
