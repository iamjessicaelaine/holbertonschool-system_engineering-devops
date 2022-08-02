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
    filename = '{}.json'.format(user_id)
    eachtasksdetails = []
    for everytask in user_tasks:
        tasksdetails = {"task": everytask.get('title'),
                        "completed": everytask.get('completed'),
                        "username": user_name}
        # append taskdetails dictionary to user's list of task details
        eachtasksdetails.append(tasksdetails)

    with open(filename, 'w') as jfile:
        users_tasks_dict = {user_id: eachtasksdetails}
        json.dump(users_tasks_dict, jfile)
