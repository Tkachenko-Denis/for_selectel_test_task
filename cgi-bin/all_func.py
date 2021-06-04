"""Функции, которые создают шутку и выводят список всех шуток заданного пользователя"""
import requests


def create_new_joke(username, joke):
    import sqlite3
    db_path = "c:/REST - API/joke_database.db"
    if joke != "Не задано":
        username_data_tuple = (username, joke)
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        sql = """INSERT INTO publication (autor, text_joke) VALUES(?,?)"""
        cur.execute(sql, username_data_tuple)
        con.commit()
        cur.close()
        con.close()
    else:
        print("Не задано")


def print_all_joke(username):
    import sqlite3
    global all_joke
    all_joke = {}
    db_path = "c:/REST - API/joke_database.db"
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("""SELECT * FROM publication""")
    for i in cur.fetchall():
        if username == i[0]:
            i = {i[2] : i[1]}
            all_joke.update(i)
    cur.close()
    con.close()
    for i in all_joke:
        print("ID:", i, "||", all_joke[i])

# фунция выводит шутку по ID
def print_one_joke_by_ID(username, ID):
    import sqlite3
    db_path = "c:/REST - API/joke_database.db"
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("""SELECT * FROM publication""")
    for i in cur.fetchall():
        if username == i[0] and ID == i[2]:
            print(i[1])
    cur.close()
    con.close()


# функция удаления рабоатает, подумать о выводе при удалении. применен новый стиль, рассмотреть
# функция удаляет шутку при введенном ID, если ID шутки и имя username совпадают в бд
def remove_joke_by_ID(username, ID):
    try:
        import sqlite3
        db_path = "c:/REST - API/joke_database.db"
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        cur.execute("""SELECT * FROM publication""")
        for i in cur.fetchall():
            if username == i[0] and ID == i[2]:
                sql = """DELETE from publication WHERE ID = ?"""
                cur.execute(sql, (ID, ))
        con.commit()
    except IndentationError as error:
        print("У Вас нет такой шутки!", error)
    finally:
        cur.close()
        con.close()


def get_API(request="https://geek-jokes.sameerkumar.website/api"):
    response = requests.get(request)
    joke_with_API = response.json()
    return joke_with_API


def update_joke(username, joke, id):
    import sqlite3
    db_path = "c:/REST - API/joke_database.db"
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("""SELECT * FROM publication""")
    for i in cur.fetchall():
        if username == i[0] and id == i[2]:
            sql = """UPDATE publication SET text_joke = ? WHERE ID = ?"""
            data = (joke, id)
            cur.execute(sql, data)
    con.commit()
    cur.close()
    con.close()


# Программа позволяет проверить, существует ли запись в базе данных
# Возвращает состояние 1 если такое имя уже есть, 0 если такого имени нет

def check_username_in_db(username):
    global STATUS_USERNAME
    STATUS_USERNAME = 0
    import sqlite3
    db_path = "c:/REST - API/joke_database.db"
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("""
    SELECT * FROM username_data
    """)
    for i in cur.fetchall():
        if username == i[0]:
            STATUS_USERNAME = 1
    cur.close()
    con.close()
    return STATUS_USERNAME


def check_username_and_password_in_db(username, password):
    global STATUS_USERNAME_AND_PASSWORD
    STATUS_USERNAME_AND_PASSWORD = 0
    import sqlite3
    db_path = "c:/REST - API/joke_database.db"
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("""
    SELECT * FROM username_data
    """)
    for i in cur.fetchall():
        if username == i[0] and password == i[1]:
            STATUS_USERNAME_AND_PASSWORD = 1
    cur.close()
    con.close()
    return STATUS_USERNAME_AND_PASSWORD

