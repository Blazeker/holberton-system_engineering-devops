#!/usr/bin/python3
""" Module for requests """

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Get the number of subs """
    header = {"User-Agent": "Blazeker"}
    url = "/hot.json?after={}".format(after)
    urlRe = "https://www.reddit.com/r/" + subreddit + url

    res = requests.get(urlRe, headers=header)

    if res.status_code == 200:
        req = res.json()
        d = req.get("data")
        children = d.get("children")
        for p in children:
            p_data = p.get("data")
            title = p_data.get("title")
            hot_list.append(title)
        after = d.get("after")
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
