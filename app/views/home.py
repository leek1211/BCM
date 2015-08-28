from flask import Flask, request, render_template, g, session 
from app import app, db
from app.decorators.user import requires_login
from app.models import User, Team
from app.forms.user import LoginForm


@app.before_request
def before_request():
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id'])


@app.route('/')
def home():
  all_teams = Team.query.all()
  for team in all_teams:
      team.memberNames= map(lambda x:str(x.name), team.members)

  rows = map(None, *(iter(all_teams),) * 3)

  return render_template("main.html", user=g.user, rows=rows)


