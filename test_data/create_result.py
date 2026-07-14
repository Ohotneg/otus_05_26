import csv
import json


# Читаем пользователей из json
with open("users.json", "r") as users_file:
    users = json.load(users_file)


# Читаем книги из csv
books = []
with open("books.csv", "r") as books_file:
    reader = csv.DictReader(books_file)
    for row in reader:
        book = {
            "title": row["Title"],
            "author": row["Author"],
            "pages": int(row["Pages"]),
            "genre": row["Genre"]
        }
        books.append(book)


# Создаем список пользователей в нужном формате
result = []
for user in users:
    new_user = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": []
    }
    result.append(new_user)


# Раздаем книги пользователям
user_index = 0
for book in books:
    result[user_index]["books"].append(book)
    user_index += 1
    if user_index == len(result):
        user_index = 0


# Записываем результат
with open("result.json", "w") as result_file:
    json.dump(
        result,
        result_file,
        indent=4
    )
