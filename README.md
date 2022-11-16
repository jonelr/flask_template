# Flask Template for New Projects

> Flask Template using Python and the following modules:

* Flask
* Flask-Brypt
* Flask-Login
* Flask-Migrate
* Flask-SQLAlchemy
* Flask-WTF

## Quick Start Using Pipenv

``` bash
# Activate venv
$ pipenv shell

# Create instance folder
$ mkdir instance

# Create config.py inside the instance folder and fill 
# with the approriate variable you wish to override from 
# the root config.py.
#
# Update the SECRET_KEY, SQLALCHEMY_DATABASE_URI to the 
# appropriate values.
$ touch instance/config.py

# Install dependencies
$ pipenv install

# Create DB
$ flask db migrate 
$ flask db upgrade

# Create first user
$ flask user create joe@example.com
>>> Adding new user...
>>> Password: 
>>> Date added: 2022-11-16 15:07:35.168473
>>> joe@example.com created

# Run Server (http://localhost:5000)
flask run
```

## Endpoints

* GET           /
* GET,POST      /login
* GET           /logout