pipenv install flask flask-login flask-wtf autopep8 flask-bcrypt
pipenv install flask-sqlalchemy
pipenv install flask-migrate

# flask migrate

flask db init
flask db migrate -m "Initial migrate"
flask db upgrade
