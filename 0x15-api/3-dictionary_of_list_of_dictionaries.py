#!/usr/bin/python3
""" Gathering information of an api """

if __name__ == "__main__":
    import requests
    import csv
    import json
    import sys

    list_aux = []
    dict_aux = {}
    file_name = "todo_all_employees.json"

    user_url = "https://jsonplaceholder.typicode.com/users/"
    url2 = requests.get(user_url)

    for users in url2.json():
        todos_api = user_url + str(users.get("id")) + "/todos"
        url1 = requests.get(todos_api)
        for i in url1.json():
            list_aux.append({"task": i.get("title"),
                             "completed": i.get("completed"),
                             "username": users.get("username")})
        dict_aux[users.get("id")] = list_aux
        list_aux = []

        with open(file_name, mode="w", encoding="utf-8") as file:
            file.write(json.dumps(dict_aux))
