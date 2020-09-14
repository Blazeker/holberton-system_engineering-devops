#!/usr/bin/python3
""" Gathering information of an api """

if __name__ == "__main__":
    import requests
    import json
    from sys import argv

    id_employees = argv[1]
    list_aux = []
    file_name = id_employees + ".json"

    todo_url = "https://jsonplaceholder.typicode.com/users/"\
               + id_employees + "/todos"
    user_url = "https://jsonplaceholder.typicode.com/users/"

    url1 = requests.get(todo_url)
    url2 = requests.get(user_url + id_employees)
    info_user = url2.json()
    name_employee = info_user.get("username")
    for i in url1.json():
        list_aux.append({"task": i.get("title"),
                         "completed": i.get("completed"),
                         "username": name_employee})
    dict_aux = {argv[1]: list_aux}
    with open(file_name, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(dict_aux))
