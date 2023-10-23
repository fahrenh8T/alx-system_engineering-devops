#!/usr/bin/python3
""" exports to-do list information for
     a given employee ID to JSON format
"""
import json
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    link = "https://jsonplaceholder.typicode.com/"

    # retrives user info
    user_reps = requests.get(link + "users/{}".format(emp_id)).json()
    username = user_reps.get("username")
    todo = requests.get(link + "todos", params={"userId": emp_id}).json()

    with open("{}.json".format(emp_id), "w") as jsonfile:
        json.dump({emp_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todo]}, jsonfile)
