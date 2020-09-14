#!/usr/bin/python3
""" Gathering information of an api """

if __name__ == "__main__":
    import requests
    import csv
    from sys import argv

    id_employees = argv[1]
    done_tasks = 0
    file_name = "USER_ID.csv"

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"

    url1 = requests.get(todo_url, params={'userId': id_employees})
    url2 = requests.get(user_url, params={'id': id_employees})
    info_user = url2.json()
    name_employee = info_user[0].get("name")

    with open(file_name, mode="w", encoding="utf-8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for i in url1.json():
            writer.writerow([str(i.get("userId")),
                             name_employee, str(i.get("completed")),
                             i.get("title")])