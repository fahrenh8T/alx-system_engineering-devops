#!/usr/bin/python3
""" function to query subscribers on a given Reddit subreddit """
import requests


def number_of_subscribers(subreddit):
    """ return the total number of subscribers on a given subreddit """
    link = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(link, headers=headers)

    if response.status_code != 200:
        return 0
    return response.json()['data']['subscribers']
