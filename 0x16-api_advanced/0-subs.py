#!/usr/bin/python3
""" Module for requests """

import requests


def number_of_subscribers(subreddit):
    """ Get the number of subs """
    header = {"User-Agent": "Blazeker"}
    urlRe = "https://www.reddit.com/r/" + subreddit + "/about.json"

    res = requests.get(urlRe, headers=header)

    if res.status_code == 200:
        return res.json().get("data").get("subscribers")
    else:
        return 0
