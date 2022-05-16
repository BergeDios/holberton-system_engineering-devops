#!/usr/bin/python3
""" Script that uses URL to get info about employee via ID given parameter """
import csv
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
    n_t = 0
    n_c = 0
    for task in json_todo:
        n_t += 1
        if task['completed'] is True:
            n_c += 1
    # Printing as nedeed name of employer num of tasks anf tasks
    print(f"Employee {json_user['name']} is done with tasks({n_c}/{n_t}:)")
    for task in json_todo:
        if task['completed'] is True:
            print(f"\t {task['title']}".expandtabs(4))
    # saving to csv format file info of employee
    filename = f'{argv[1]}.csv'
    csv_list = []
    for task in json_todo:
        csv_list.append([argv[1], json_user['username'],
                         task['completed'], task['title']])
    with open(filename, mode='w') as file:
        file_writer = csv.writer(file,
                                 delimiter=',',
                                 quotechar='"',
                                 quoting=csv.QUOTE_ALL)

        for item in csv_list:
            file_writer.writerow(item)
