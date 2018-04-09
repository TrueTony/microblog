from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Anton'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie wa cool!'
        },
        {
            'author': {'username': 'Иполит'},
            'body': 'Is`s so disgusting, your fish in oil!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

