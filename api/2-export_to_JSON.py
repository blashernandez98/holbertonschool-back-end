#!/usr/bin/python3
""" Task 2 module """

if __name__ == '__main__':

    import requests
    import json
    from sys import argv

    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.
        format(argv[1])).json()

    todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.
        format(argv[1])).json()

    list_todos = []
    for todo in todos:
        list_todos.append(
            {"task": todo.get('title'),
             "completed": todo.get('completed'),
             "username": user.get('username')})

    json_dic = {str(argv[1]): list_todos}

    with open('{}.json'.format(argv[1]), 'w') as f:
        json.dump(json_dic, f)
