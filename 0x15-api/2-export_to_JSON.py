#!/usr/bin/python3
""" Gathering information of an api """

if __name__ == "__main__":
    import requests
    import csv
    import json
    from sys import argv

    id_employees = argv[1]
    list_aux = []
    file_name = "USER_ID.json"

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"

    url1 = requests.get(todo_url, params={'userId': id_employees})
    url2 = requests.get(user_url, params={'id': id_employees})
    info_user = url2.json()
    name_employee = info_user[0].get("name")

    for i in url1.json():
        list_aux.append({"task": i.get("title"),
                        "completed": i.get("completed"),
                        "username": i.get(name_employee)})
    dict_aux = {argv[1]: list_aux}
    with open(file_name, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(dict_aux))
