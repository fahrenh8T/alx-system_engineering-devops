#!/usr/bin/python3
""" using REST API, for a given employee ID, returns information about his/her TODO list progress """
import requests
from sys import argv


if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com/"
    userid = requests.get(link + "users/{}".format(argv[1])).json()
    todo = requests.get(link + "todos", params={"userId": argv[1]}).json()

    done = [req.get("title") for req in todo if req.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(userid.get("name"),
          len(done), len(todo)))
    [print("\t {}".format(com)) for com in done]
