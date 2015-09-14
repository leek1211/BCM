from flask import Blueprint, request, flash, render_template, g, session, redirect, url_for

from app import db,tmdb
from app.decorators.user import requires_login
from app.models import Review, User

mod = Blueprint('review', __name__)

@mod.before_request
def before_request():
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id'])

@mod.route('/review/<movie_id>/', methods=['POST'])
@requires_login
def review_rate(movie_id):
    if not (request.form['rating']) :
        return redirect(url_for('movie.movie_info', id=movie_id))

    rating = int(request.form['rating'])
    myReview = g.user.get_review(movie_id) 
    if myReview:
        myReview.rating = rating
        db.session.commit()
    else :
        review = Review(movie_id=movie_id, user_id=g.user.id, rating=rating)
        db.session.add(review)
        g.user.reviews.append(review)
        db.session.commit()

    return redirect(url_for('movie.movie_info', id=movie_id))