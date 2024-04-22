#!/usr/bin/python3
"""a script that uses a REST API to get info on all employee about their
   TODO list progress and exports it in JSON format.
"""
import json
import requests


def get_employees_info():
    """gets the info of all employees"""
    users_api = 'https://jsonplaceholder.typicode.com/users'
    todos_api = 'https://jsonplaceholder.typicode.com/todos'

    users = requests.get(users_api)
    todos = requests.get(todos_api)
    if users.status_code == 200 and todos.status_code == 200:
        usernames_and_ids = {}
        for user in users.json():
            usernames_and_ids[str(user.get('id'))] = user.get('username')
        all_employees = {}
        for todo in todos.json():
            userId = str(todo.get('userId'))
            if all_employees.get(userId, None) is None:
                all_employees[userId] = []
            all_employees[userId].append({
                        "username": usernames_and_ids.get(userId),
                        "task": todo.get('title'),
                        "completed": todo.get('completed')
                    })
        file_name = 'todo_all_employees.json'
        with open(file_name, 'w') as file:
            json.dump(all_employees, file)


if __name__ == '__main__':
    get_employees_info()
