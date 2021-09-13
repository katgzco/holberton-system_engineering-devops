#!/usr/bin/python3
"""Returns information about given employee ID and TODO list progress.
    """
import json
import requests
from sys import argv

if __name__ == "__main__":

    completed_task = list()

    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    all_employes = dict()

    for user in users:
        todo = requests.get(
            url + "todos", params={"userId": user.get('id')}).json()
        employe = list()
        for task in todo:
            employe.append({
                "username": user.get("name"),
                "task": task.get("title"),
                "completed": task.get("completed"),
            })

        all_employes.update({user.get('id'): employe})

    with open('todo_all_employees.json', mode='w') as file:
        json.dump(all_employes, file)
