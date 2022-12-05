#!/usr/bin/python3
""" Task 3 module """

if __name__ == '__main__':

    import requests
    import json
    from sys import argv

    users = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    json_dic = {}

    for user in users:
        list_todos = []
        todos = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.
            format(user.get('id'))).json()

        for todo in todos:
            list_todos.append(
                {"task": todo.get('title'),
                 "completed": todo.get('completed'),
                 "username": user.get('username')})

        json_dic[user.get('id')] = list_todos

    with open('todo_all_employees.json', 'w') as f:
        json.dump(json_dic, f)
