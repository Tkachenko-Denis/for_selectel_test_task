# Программа регистрации нового пользователя
# Принимает на вход новый логи и пароль, выдает ошибки в случае когда:
# 1) логин меньше 5 символов
# 2) Пароль меньше 8 символов
# 3) Пользователь с таким именем уже существует
# Возвращает state_counter - счетчик состояния, который указывает на действие

def register_new_user(username, password):
    import sqlite3
    from all_func import check_username_in_db
    global state_counter
    state_counter = 0
    username_data_list = []
    db_path = "c:/REST - API/joke_database.db"
    con = sqlite3.connect(db_path)
    if username == "":
        print("Error! Вы ничего не ввели!")
        state_counter = 0
    elif len(username) < 5:
        print("Error! Придумай логин больше 5 символов")
        state_counter = 0
    elif password == "":
        print("Error! Вы не ввели пароль!")
        state_counter = 0
    elif len(password) < 7:
        print("Error! Пароль меньше 8 символов не допустим!")
        state_counter = 0
    elif check_username_in_db(username) == 1:
        print("Такой  пользователь существует!")
        state_counter = 0
    else:
        username_data_list.append(username)
        username_data_list.append(password)
        cur = con.cursor()
        sql = """\
                    INSERT INTO username_data VALUES(?,?)
                        """
        cur.execute(sql, username_data_list)
        print("Добавлен!")
        con.commit()
        cur.close()
        con.close()
        state_counter = 1
    return state_counter
