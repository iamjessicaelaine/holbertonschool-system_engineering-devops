#!/usr/bin/python3
"""for a given employee ID, returns info about emp.'s todo list progress"""

# Standard library imports
import requests
from sys import argv

api_url_base = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    # if type(argv[1]) == int:  # check to make sure parameter is an int
    employee_id = int(argv[1])
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
