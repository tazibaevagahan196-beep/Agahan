# Импортируем класс Flask и функцию render_template из модуля flask
from flask import Flask, render_template

# Создаём экземпляр веб-приложения Flask. __name__ определяет имя текущего модуля
app = Flask(__name__)

# Декоратор @app.route связывает URL-адрес '/' (корневой) с функцией hello_world
@app.route('/')
# Определяем функцию-обработчик для корневого маршрута
def hello_world():
    # Возвращаем HTML-шаблон 'index.html', который должен находиться в папке templates
    return render_template("index.html")

# Запускаем встроенный веб-сервер Flask. Параметр '0.0.0.0' делает сервер доступным извне (не только с localhost)
app.run("0.0.0.0")