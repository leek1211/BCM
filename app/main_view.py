from flask import Flask, request, render_template, g, session 
from app import app, db
from app.users.decorators import requires_login
from app.users.models import User
from app.users.forms import LoginForm
from app.teams.models import Team


@app.before_request
def before_request():
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id'])


@app.route('/')
def home():
  all_teams = Team.query.all()
  for team in all_teams:
      team.captainName = User.query.filter_by(id=team.captain).first().name

  rows = map(None, *(iter(all_teams),) * 3)

  return render_template("main.html", user=g.user, rows=rows)


