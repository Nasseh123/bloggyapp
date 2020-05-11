from flask import render_template,request,redirect,url_for
from .import main
from flask_login import login_required
@main.route('/')
@login_required
def index():
    """
    """

    title="Blog App"
    message="Welcome to blog app"
    return render_template('index.html',title=title,message=message)