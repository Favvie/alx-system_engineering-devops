#!/usr/bin/python3
"""
api module
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user_response = requests.get("https://jsonplaceholder\
                                  .typicode.com/users/{}".format(user_id))
    todo_response = requests.get("https://jsonplaceholder.typicode.com/todos")

    username = user_response.json()["name"]

    data = todo_response.json()
    count_task = 0
    count_completed = 0
    for item in data:
        if item["userId"] == int(user_id):
            if item["completed"]:
                count_completed = count_completed + 1
            count_task = count_task + 1
    print("Employee {} is done with tasks({}/{})"
          .format(username, count_completed, count_task))

    for item in data:
        if item["userId"] == int(user_id):
            if item["completed"]:
                print("\t{}".format(item["title"]))
