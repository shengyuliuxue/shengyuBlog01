import functools

from flask import(
    Blueprint, flash, g, current_app, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('posts', __name__, url_prefix='/posts')

@bp.route('/post')
def post():
    render_template('posts/post.html')
