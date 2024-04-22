#!/usr/bin/python3
"""a script that uses a REST API to get info on a given employee ID about their
   TODO list progress and exports it in CSV format.
"""
import csv
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
        info = []
        for todo in todos:
            info.append([eid, username,
                        todo.get('completed'),
                        todo.get('title')])
        file_name = '{}.csv'.format(eid)
        with open(file_name, 'w', newline='') as f:
            file = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
            file.writerows(info)


if __name__ == '__main__':
    if len(argv) == 2 and argv[1].isdigit():
        get_employee_info(argv[1])
