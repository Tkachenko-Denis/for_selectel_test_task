from register_func import register_new_user
import cgi
import html

form = cgi.FieldStorage()
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title> Registration </title>
                <style>
        h1 {
            margin: 0 auto;
            padding: 1em;
            width: 400px;
        }
        form {
          margin: 0 auto;
          width: 400px;
          padding: 1em;
          border: 1px solid #CCC;
          border-radius: 1em;
        }
        ul {
          list-style: none;
          padding: 1em;
          margin: 0 auto;
          width: 400px;
        }
        input{
          width: 400px;
          box-sizing: border-box;
          border: 1px solid #999;
          }
    </style>
        </head>
        <body>""")
print('<h1>')
print('Зарегистрируйтесь')
print('</h1>')
print('<form method="post">')
print('Имя пользователя <input type="text" name="new_username">')
print('Пароль <input type="text" name="new_password">')
print('<button type="submit" name="reg_buttom" value="Регистрация"> Регистрация </button>')
print('<button type="reset">Очистить</button>')
print('<br>')
if "reg_buttom" in form:
    text_1 = form.getfirst("new_username", "")
    text_1 = html.escape(text_1)
    text_2 = form.getfirst("new_password", "")
    text_2 = html.escape(text_2)
    if register_new_user(text_1, text_2) == 0:
        print("Попробуйте еще")
    else:
        print("Пользователь добавлен!")
print('</form>')
print('<ul>')
print('<li>')
print('<button type="button">')
print('<a href="..">Вернуться</a>')
print('</button>')
print('</li>')
print('</ul>')

print("""</body>
        </html>""")
