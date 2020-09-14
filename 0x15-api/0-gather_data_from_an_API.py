#!/usr/bin/python3
""" Gathering information of an api """

if __name__ == "__main__":
    import requests
    from sys import argv

    id_employees = argv[1]
    list_done_tasks = []

    todo_url = "https://jsonplaceholder.typicode.com/"
    user_url = "https://jsonplaceholder.typicode.com/users/"

    url1 = requests.get(todo_url + "todos?userId=" + id_employees)
    url2 = requests.get(user_url + id_employees)
    info_user = url2.json()
    name_employee = info_user.get("name")

    for tasks in url1.json():
        if tasks.get("completed") is True:
            list_done_tasks.append(tasks)
    print("Employee {} is done with tasks ({}/{}):".
          format(name_employee, len(list_done_tasks), len(url1.json())))
    for tasks in list_done_tasks:
        print("\t {}".format(tasks.get("title")))
