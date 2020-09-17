#!/usr/bin/python3
""" Module for requests """

import requests
import sys


def top_ten(subreddit):
    """ Get the top ten posts """
    header = {"User-Agent": "Blazeker"}
    urlRe = "https://www.reddit.com/r/" + subreddit + "/hot.json"

    res = requests.get(urlRe, headers=header).json()

    if res.get('error') == 404:
        print("None")
        return

    resp = res.get("data").get("children")

    for i, p in enumerate(resp[:10]):
        print(p.get("data").get("title", None))
