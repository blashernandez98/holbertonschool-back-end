#!/usr/bin/python3
""" Task 1 module """

import csv
from requests import get
from sys import argv

user = get(
    'https://jsonplaceholder.typicode.com/users/{}'.
    format(argv[1])).json()

todos = get(
    'https://jsonplaceholder.typicode.com/users/{}/todos'.
    format(argv[1])).json()

file_name = '{}.csv'.format(user.get('id'))

with open(file_name, 'w') as f:
    writer = csv.writer(f)
    for task in todos:
        writer.writerow([
            user.get('id'),
            user.get('username'),
            task.get('completed'),
            task.get('title')
        ])
