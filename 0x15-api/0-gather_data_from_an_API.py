#!/usr/bin/python3
""" Gathering information of an api """

if __name__ == "__main__":
    import requests
    from sys import argv

    id_employees = argv[1]
    done_tasks = 0

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"

    url1 = requests.get(todo_url)
    url2 = requests.get(user_url, params={'id': id_employees})
    info_user = url2.json()
    name_employee = info_user[0].get("name")

    for tasks in url1.json():
        if tasks.get("completed") is True:
            done_tasks += 1
    print("Employee {} is done with tasks ({}/{}):".
          format(name_employee, done_tasks, len(url1.json())))
    for tasks in url1.json():
        if tasks.get("completed") is True:
            print("\t {}".format(tasks.get("title")))
