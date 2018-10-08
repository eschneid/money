from flask import Flask
from flask import render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from forms import LoginForm

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Shelly'}

    posts = [
        {
            'author': {'username': 'Eric'},
            'body': 'Deposited Money in Chase!'
        },
        {
            'author': {'username': 'Shelly'},
            'body': 'Deposited Money in Huntington!'
        }
    ]



    return render_template('index.html', title='Home', user=user, posts=posts)

if __name__ == '__main__':
    app.run()
