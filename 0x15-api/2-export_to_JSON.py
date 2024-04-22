#!/usr/bin/python3
"""a script that uses a REST API to get info on a given employee ID about their
   TODO list progress and exports it in CSV format.
"""
import json
import requests
from sys import argv


def get_employee_info(eid):
    url = 'https://jsonplaceholder.typicode.com'
    users_api = url + f'/users/{eid}'
    todos_api = url + f'/todos?userId={eid}'

    user = requests.get(users_api)
    todos = requests.get(todos_api)
    if user.status_code == 200 and todos.status_code == 200:
        username = user.json().get('username', None)
        todos = todos.json()
        info = {eid: []}
        for todo in todos:
            info[eid].append({
                    "task": todo.get('title'),
                    "completed": todo.get('completed'),
                    "username": username
                    })
        file_name = '{}.json'.format(eid)
        with open(file_name, 'w') as file:
            json.dump(info, file)


if __name__ == '__main__':
    if len(argv) == 2 and argv[1].isdigit():
        get_employee_info(argv[1])
