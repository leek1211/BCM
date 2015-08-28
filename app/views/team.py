from flask import Blueprint, request, flash, render_template, g, session, redirect, url_for

from app import db
from app.decorators.user import requires_login
from app.models import User, Team
from app.forms.team import RegisterForm
mod = Blueprint('team', __name__,url_prefix='/team')

@mod.before_request
def before_request():
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id'])

@mod.route('/<teamid>/')
@requires_login
def team_page(teamid):
    team = Team.query.filter_by(id=teamid).first_or_404()
    members = team.members

    return render_template('team/team_page.html', team=team, members=members)

@mod.route('/register/', methods = ['GET', 'POST'])
@requires_login
def team_register():
    """
    Register form
    """
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        newTeam = Team(name=form.name.data, captain=g.user.id)
        newTeam.members.append(g.user)
        db.session.add(newTeam)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('team/register.html', form=form)

@mod.route('/<teamid>/apply/', methods = ['POST'])
@requires_login
def team_apply(teamid):
    team = Team.query.filter_by(id=teamid).first_or_404()

    member_ids = map(lambda x: int(x.id), team.members)
    cur_user_id = g.user.id

    if member_ids.count(g.user.id) == 0: 
        team.members.append(g.user)
        db.session.commit()
    else : flash('You are already in the team')
    return redirect(url_for('team.team_page', teamid=teamid))
