from flask import Blueprint, request, flash, render_template, g, session, redirect, url_for

from app import db
from app.decorators.user import requires_login
from app.models import User
from app.forms.team import RegisterForm
mod = Blueprint('movie', __name__)


import tmdbsimple as tmdb
tmdb.API_KEY = '9b28b589e4b6afc064926f2e8af69d27'

@mod.before_request
def before_request():
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id'])

@mod.route('/search/<title>/')
@requires_login
def movie_search(title):
    search = tmdb.Search()
    response = search.movie(query=title)
    if response['total_results'] > 100:
        response['results'] = response['results'][0:100]

    return render_template('movie/search.html', res=response)

