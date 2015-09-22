from flask import Flask, request, render_template, g, session 
from app import app, db, tmdb
from app.decorators.user import requires_login
from app.models import User
from app.forms.user import LoginForm

@app.before_request
def before_request():
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id'])


@app.route('/')
@requires_login
def home():
  movies = tmdb.Movies('popular').info()['results'][1:20]

  rows = map(None, *(iter(movies),) * 3)

  return render_template("main.html", user=g.user, rows=rows)


