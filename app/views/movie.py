from flask import Blueprint, request, flash, render_template, g, session, redirect, url_for

from app import db,tmdb
from app.decorators.user import requires_login
from app.models import User
from app.machineLearning import logistic_regression
import numpy

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
    response = search.movie(query=title, page=1)

    rows = map(None, *(iter(response['results']),) * 3)

    return render_template('movie/search.html', total_results=response['total_results'], rows=rows)

@mod.route('/movie/<id>/')
@requires_login
def movie_info(id):
    m = tmdb.Movies(id)
    return render_template('movie/info.html', movie=m.info(), casts=m.credits()['cast'], crews=m.credits()['crew'], review=g.user.get_review(id))

@mod.route('/recommend/')
@requires_login
def movie_recommend(): 
    movies = tmdb.Movies('popular').info()['results']

    myMovies = numpy.empty((0,0)) 
    myScores = numpy.empty((0,0))
    for review in g.user.reviews :
        myMovies = numpy.append(myMovies, review.get_movie().info())
        myScores = numpy.append(myScores, review.rating/10)
    
    pred_scores = logistic_regression.run(myMovies, myScores)

    for (m, sc) in zip(movies, pred_scores) :
        m['expected'] = round(sc*10, 1)

    val =  numpy.transpose([map(lambda x: x['title'], movies) , pred_scores])
    print val
    
    rows = map(None, *(iter(movies),) * 3)

    return render_template('movie/recommend.html', rows=rows )
