#!/usr/bin/python3
"""a script that uses a REST API to get info on a given employee ID about their
   TODO list progress.
"""
import requests
from sys import argv


def get_employee_info(eid):
    url = 'https://jsonplaceholder.typicode.com'
    users_api = url + f'/users/{eid}'
    todos_api = url + f'/todos?userId={eid}'

    name = requests.get(users_api)
    todos = requests.get(todos_api)
    if name.status_code == 200 and todos.status_code == 200:
        name = name.json().get('name', None)
        todos = todos.json()
        titles = []
        done, total = 0, 0
        for todo in todos:
            titles.append(todo.get('title'))
            if todo.get('completed') == 'true':
                done += 1
            total += 1

        print('Employee {} is done with tasks({}/{}):'.format(name,
                                                              done, total))
        for title in titles:
            print('\t {}'.format(title))


if __name__ == '__main__':
    if len(argv) == 2 and type(argv[2]) is int:
        get_employee_info(argv[2])
