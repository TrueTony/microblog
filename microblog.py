from app import app, db, cli
from app.models import User, Post


@app.shell_context_processor
def make_shell_contect():
    return {'db': db, 'User': User, 'Post': Post}

# https://habrahabr.ru/post/346306/