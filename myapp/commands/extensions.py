# myapp/commands/extensions.py

from flask import Blueprint, current_app
import click
from getpass import getpass
from myapp.models import db, User
from flask_bcrypt import Bcrypt

user_bp = Blueprint("user_bp", __name__, cli_group="user")


@user_bp.cli.command("create")
@click.argument("email")
def create(email):
    """Creates a new user using the provided email address

    :param email: The email address that will be used to create the new user account
    """

    bcrypt = Bcrypt()
    bcrypt.init_app(current_app)

    print("Adding new user...")
    email = email
    password = getpass("Password: ")

    user = User(email=email, password=bcrypt.generate_password_hash(
        password).decode('utf-8'))

    db.session.add(user)
    db.session.commit()
    print(f"Date added: {user.date_added}")
    print(f"{email} created")
