#!/usr/bin/python3
"""
a module  that export to csv file
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(url)
    todo_response = requests.get(url + "/todos")

    username = user_response.json()["name"]

    data = todo_response.json()

    item_arr = []
    for item in data:
        arr = []
        arr.append(str(item["userId"]))
        arr.append(str(username))
        arr.append(item["completed"])
        arr.append(item["title"])
        item_arr.append(arr)

    header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    with open(f"{user_id}.csv", "w", encoding="UTF-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(item_arr)
