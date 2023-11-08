#!/usr/bin/python3
""" function to print hot posts on a given Reddit subreddit """
import requests


def top_ten(subreddit):
    """ print the titles of the 10 hottest posts on a given subreddit """
    link = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced"
    }
    para = {
        "limit": 10
    }
    response = requests.get(link, headers=headers, params=para,
                            allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
