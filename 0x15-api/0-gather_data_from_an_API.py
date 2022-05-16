#!/usr/bin/python3
""" Script that uses URL to get info about employee
    via ID given as parameter """
import requests
from sys import argv

if __name__ == "__main__":
    # Forming url for specific user and getting the body
    # of the response into json format in a variable
    user = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    user_resp = requests.get(user)
    json_user = user_resp.json()
    # Forming url for todo list for user and saving json response
    # of body into variable
    todos = f'{user}/todos'
    todos_resp = requests.get(todos)
    json_todo = todos_resp.json()

    # Counting number of tasks total and completed
    n_tasks = 0
    n_comp = 0
    for task in json_todo:
        n_tasks += 1
        if task['completed'] == True:
            n_comp += 1
    # Printing as nedeed
    print(f"Employee {json_user['name']} is done with tasks({n_comp}/{n_tasks}:)")
    for task in json_todo:
        if task['completed'] == True:
            print(f"\t {task['title']}")
