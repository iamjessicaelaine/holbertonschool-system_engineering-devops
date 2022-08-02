#!/usr/bin/python3
"""for a given employee ID, returns info about emp.'s todo progress"""

# Standard library imports
import json
import requests
from sys import argv


if __name__ == '__main__':
    api_url_base = 'https://jsonplaceholder.typicode.com'
    employee_id = argv[1]
    # gettig cotent from response obj received from user id url
    employee_data = requests.get('{}/users/{}'.format(api_url_base,
                                                      employee_id)).json()
    # get the employee name
    employee_name = employee_data.get('name')
    # get employee to do list
    employee_todos = requests.get('{}/users/{}/todos'.format(api_url_base,
                                                             employee_id))
    # turn employee to do response obj into json content
    todolist = employee_todos.json()
    totaltasks = len(todolist)  # get total number of tasks
    completedlist = []  # need an empty list hold done tasks for printing
    for taskdict in todolist:  # iterate through each task for needed info
        tasktitle = taskdict.get('title')
        if taskdict.get('completed') is True:  # if task is done...
            completedlist.append(tasktitle)  # ...add it to completed list
        else:
            continue
    totaltasksdone = len(completedlist)
    # print to stdout in specified format
    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
                                                          totaltasksdone,
                                                          totaltasks))
    if totaltasksdone > 0:
        for donetask in completedlist:
            print('\t {}'.format(donetask))
