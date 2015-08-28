from flask import Blueprint, request, flash, render_template, g, session, redirect, url_for

from app import db
from app.users.decorators import requires_login
from app.users.models import User
from app.teams.models import Team
from app.teams.forms import RegisterForm
mod = Blueprint('teams', __name__,url_prefix='/team')

@mod.before_request
def before_request():
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id'])

@mod.route('/<teamid>/')
@requires_login
def team_page(teamid):
    team = Team.query.filter_by(id=teamid).first_or_404()
    captain = User.query.filter_by(id=team.captain).first()

    return render_template('teams/team_page.html', team=team, captain=captain)

@mod.route('/register/', methods = ['GET', 'POST'])
@requires_login
def team_register():
    """
    Register form
    """
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        newTeam = Team(name=form.name.data, captain=g.user.id)
        db.session.add(newTeam)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('teams/register.html', form=form)


