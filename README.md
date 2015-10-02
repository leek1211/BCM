# MRS
Movie recommendation system

This application fetches data from "The Movie Database(TMDb)"
You need the API_KEY generated from TMDb, and set it up in config.py.


### How to install
Install libraries:

`sudo pip install Flask-SQLAlchemy`

`sudo pip install flask-wtf`

`sudo pip install tmdbsimple

Create db table by following:

`python shell.py`

`>>> from app import db`

`>>> db.create_all()`

### How to run it

`python run.py`
