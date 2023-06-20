from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/', methods=['GET', 'POST'])
def order():
    return render_template('main.html', title='Авторизация')

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    return render_template('contacts.html', title='Авторизация')

# если чето из файла надо будет извлекать
# @app.route('/news')
# def news():
#     with open("news.json", "rt", encoding="utf8") as f:
#         news_list = json.loads(f.read())
#     print(news_list)
#     return render_template('news.html', news=news_list)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')