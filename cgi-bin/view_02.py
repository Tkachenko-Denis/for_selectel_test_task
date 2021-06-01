import cgi
import html
from all_func import create_new_joke, print_all_joke, print_one_joke_by_ID, remove_joke_by_ID, get_API
from all_func import update_joke, check_username_and_password_in_db


form = cgi.FieldStorage()
username = form.getvalue("username", "")
username = html.escape(username)
password = form.getvalue("password", "")
password = html.escape(password)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title> Личный кабинет </title>
            <style>
        h1 {
            margin: 0 auto;
            padding: 1em;
            width: 400px;
        }
        p {
            margin: 0 auto;
            padding: 1em;
            width: 400px;
        }
        form {
          margin: 0 auto;
          width: 600px;
          padding: 1em;
          border: 2px solid #CCC;
          border-radius: 1em;
        }

    </style>
        </head>
        <body>""")
if check_username_and_password_in_db(username, password) == 0:
    print("Такого пользователя нет! Зарегистрируйтесь или попробуйте заново!")
    print('<ul>')
    print('<li>')
    print('<button type="button">')
    print('<a href="..">Вернуться</a>')
    print('</button>')
    print('</li>')
    print('</ul>')

elif check_username_and_password_in_db(username, password) == 1:
    print("<h1> Привет, %s! </h1>"%username)
    print("<p> Добро пожаловать, это твоя личная страничка с шутками.</p>")

    # Часть 1, которая записывает введенные в поле шутки: Начало
    print('<form method="post">')
    print('<input type="submit" name="write_joke" value="Записать шутку">')
    print("<br>")
    print('<textarea rows="10" cols="60" name="post_text_joke" value="Введите свою шутку">')
    print('</textarea>')
    # При нажатии на кнопку "Записать шутку" функиция формы записывает в переменную значение из поля
    # "post_text_joke", затем происходит вызов фунции create_new_joke, в которую передаются значения из текстового поля
    # и username пользователя
    if "write_joke" in form:
        post_joke = form.getvalue("post_text_joke", "Не задано")
        post_joke = html.escape(post_joke)
        create_new_joke(username, post_joke)
    print('</form>')
    print("<br>")
    # Часть 1: Конец

    # Часть 2, которая выводит и записывает выведенные в поле шутки: Начало
    print('<form method="post">')
    print('<input type="submit" name="get_API_joke" value="Вывести случайную шутку">')
    print('<input type="submit" name="write_joke_by_API" value="Записать шутку">')
    print('<input type="submit" name="clear_textarea" value="Очистить">')
    print("<br>")
    print('<textarea rows="5" cols="60" readonly="readonly" name="joke_API">')
    if "get_API_joke" in form:
        print(get_API())
    elif "write_joke_by_API" in form:
        joke_by_API = form.getvalue("joke_API", "Не задано")
        joke_by_API = html.escape(joke_by_API)
        create_new_joke(username, joke_by_API)
    elif "clear_textarea" in form:
        print('')
    print('</textarea>')
    print('</form>')
    print("<br>")
    # Часть 2: Конец

    # Часть 3, которая выводит в поле все шутки данного пользователя: Начало
    print('<form method="post">')
    print('<input type="submit" name="print_all_joke" value="Показать все шутки">')
    print('<input type="submit" name="hide_all_joke" value="Скрыть все шутки">')
    print("<br>")
    print('<textarea readonly="readonly" rows="10" cols="60">')
    if "print_all_joke" in form:
        print_all_joke(username)
    elif "hide_all_joke" in form:
        print('')
    print('</textarea>')
    print('</form>')
    print("<br>")
    # Часть 3: Конец

    # Часть 4: Начало
    print('<form method="post">')
    print('<input type="text" name="get_ID" size="4">')
    print('<input type="submit" name="print_one_joke_by_ID" value="Найти шутку по ID">')
    print('<input type="submit" name="delete_one_joke_by_ID" value="Удалить шутку по ID">')
    print('<br>')
    print('<textarea rows="3" cols="60" name="taken_joke_by_ID">')
    if "print_one_joke_by_ID" in form:
        taken_ID = form.getvalue("get_ID")
        taken_ID = html.escape(taken_ID)
        print_one_joke_by_ID(username, int(taken_ID))
    elif "delete_one_joke_by_ID" in form:
        taken_ID = form.getvalue("get_ID")
        taken_ID = html.escape(taken_ID)
        remove_joke_by_ID(username, int(taken_ID))
    print("</textarea>")
    print('</form>')
    print("<br>")
    # Часть 4: Конец

    # Часть 5: Начало
    print('<form method="post">')
    print('<input type="text" name="get_ID" size="4">')
    print('<input type="submit" name="update_joke" value="Обновить шутку по ID">')
    print('<br>')
    print('<textarea rows="5" cols="60" name="get_text_joke">')
    print("</textarea>")
    if "update_joke" in form:
        taken_for_update = form.getvalue("get_text_joke")
        taken_for_update = html.escape(taken_for_update)
        taken_ID = form.getvalue("get_ID")
        taken_ID = html.escape(taken_ID)
        update_joke(username, taken_for_update, int(taken_ID))
    print('</form>')
    print("<br>")
    # Часть 5: Конец

    print('<ul>')
    print('<li>')
    print('<button type="button name="exit_in_form">')
    print('<a href="..">Выйти</a>')
    print('</button>')
    if "exit_in_form" in form:
        username = ""
        password = ""
    print('</li>')
    print('</ul>')

print("""</body>
        </html>""")
