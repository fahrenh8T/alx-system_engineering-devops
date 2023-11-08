#!/usr/bin/python3
""" function to query subscribers on a given Reddit subreddit """
import requests


def number_of_subscribers(subreddit):
    """ return the total number of subscribers on a given subreddit """
    link = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced"}
    response = requests.get(link, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
