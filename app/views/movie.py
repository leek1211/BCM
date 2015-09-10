from flask import Blueprint, request, flash, render_template, g, session, redirect, url_for

from app import db,tmdb
from app.decorators.user import requires_login
from app.models import User
mod = Blueprint('movie', __name__)

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

@mod.route('/movie/<id>/')
@requires_login
def movie_info(id):
    m = tmdb.Movies(id)
    return render_template('movie/info.html', movie=m.info(), credits = m.credits(), review=g.user.get_review(id))
