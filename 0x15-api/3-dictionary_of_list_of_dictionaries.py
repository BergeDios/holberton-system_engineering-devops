#!/usr/bin/python3
""" Script that uses URL to get info about employee via ID given parameter """
import json
import requests
from sys import argv

if __name__ == "__main__":
    # Forming url for all users and getting the body
    # of the response(users dicts) into json format in a variable
    users = f'https://jsonplaceholder.typicode.com/users'
    users_resp = requests.get(users)
    json_users = users_resp.json()
    # Creating dicionary to dump into json file with all
    # users info about todos and username
    dict_users_tasks = {}
    for user in json_users:
        userid = user.get('id')
        todo_url = f'{users}/{userid}/todos'
        todo_resp = requests.get(todo_url)
        tasks = todo_resp.json()
        list_tasks = []
        for task in tasks:
            dict_per_task = {"username": user['username'],
                             "task": task['title'],
                             "completed": task['completed']}
            list_tasks.append(dict_per_task)
        dict_users_tasks[userid] = list_tasks
    # Saving to json
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as file:
        json.dump(dict_users_tasks, file)
