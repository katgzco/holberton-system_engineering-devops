#!/usr/bin/python3
"""Returns information about given employee ID and TODO list progress.
    """
import csv
import requests
import sys

if __name__ == "__main__":
    """Using what you did in the task #0, extend your Python script
    to export data in the CSV format.
    """

    completed_task = list()

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    user_id = sys.argv[1]
    username = user.get("name")

    filename = "{}.csv".format(user_id)
    with open(filename, mode='w') as file:
        writer = csv.writer(file, delimiter=',',
                            quoting=csv.QUOTE_ALL)

        for task in todo:
            writer.writerow([user_id, username, task.get(
                "completed"), task.get("title")])
