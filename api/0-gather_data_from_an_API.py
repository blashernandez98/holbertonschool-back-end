#!/usr/bin/python3
""" Task 0 module """

if __name__ == '__main__':
    import requests
    from sys import argv

    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])).json()

    completed = []
    for todo in todos:
        if todo.get('completed'):
            completed.append(todo.get('title'))

    print("Emplyee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completed), len(todos)
    ))

    for task in completed:
        print('\t{}'.format(task))
