#!/usr/bin/python3
"""script exports all tasks owned by employee in CSV format"""


import csv
import json
import requests
from sys import argv


if __name__ == '__main__':
    user_url = 'https://jsonplaceholder.typicode.com/users'
    user_id = argv[1]
    user_data = requests.get('{}/{}'.format(user_url, user_id)).json()
    user_name = user_data.get('username')
    user_tasks = requests.get('{}/{}/todos'.format(user_url, user_id)).json()
    # completeTorF = user_tasks.get('completed')
    # task_title = user_tasks.get('title')
    filename = '{}.csv'.format(user_id)
    # taskrow = [user_id, user_name, completeTorF, task_title]
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for everytask in user_tasks:
            completeTorF = everytask.get('completed')
            task_title = everytask.get('title')
            taskrow = [user_id, user_name, completeTorF, task_title]
            writer.writerow(taskrow)
