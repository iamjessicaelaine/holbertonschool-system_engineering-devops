#!/usr/bin/python3
"""script exports all tasks owned by employee in CSV format"""


import json
import requests


if __name__ == '__main__':
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    allusers = requests.get(users_url).json()
    for user in allusers:
        usertaskurl = '{}/{}
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
