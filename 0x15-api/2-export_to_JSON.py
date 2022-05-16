#!/usr/bin/python3
""" Script that uses URL to get info about employee via ID given parameter """
import json
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

    # saving to file in json format

    # forming dictionary in correct format
    list_tasks = []
    for task in json_todo:
        task_dict = {"task": task['title'],
                     "completed": task['completed'],
                     "username": json_user['username']}
        list_tasks.append(task_dict)
    dict_user_tasks = {argv[1]: list_tasks}
    # saving
    filename = f'{argv[1]}.json'
    with open(filename, mode='w') as file:
        json.dump(dict_user_tasks, file)
