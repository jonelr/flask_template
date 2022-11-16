import sys
from getpass import getpass

from flask import Flask
from flask_bcrypt import Bcrypt

from myapp.models import User, db
from myapp import create_app


def main():
    app = create_app()
    bcrypt = Bcrypt()
    bcrypt.init_app(app)

    print("Adding new user...")
    email = input("Email address: ")
    password = getpass("Password: ")

    user = User(email=email, password=bcrypt.generate_password_hash(
        password).decode('utf-8'))

    with app.app_context():
        db.session.add(user)
        db.session.commit()
        print(f"Date added: {user.date_added}")


if __name__ == "__main__":
    sys.exit(main())
