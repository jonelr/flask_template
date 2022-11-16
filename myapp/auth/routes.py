# myapp/auth/routes.py

from flask import render_template, request, redirect, url_for
from flask_login import (login_required,
                         logout_user, login_user, current_user)
from myapp.forms import LoginForm
from myapp.models import session, User
from myapp.auth.extensions import login_manager, bcrypt, auth_bp


@login_manager.user_loader
def load_user(user_id):
    return session.get(User, user_id)


@auth_bp.route('/logout', methods=['GET'])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    session.add(user)
    session.commit()
    logout_user()
    return render_template('auth/logout.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = session.get(User, form.email.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                session.add(user)
                session.commit()
                login_user(user)

                next = request.args.get('next')

                return redirect(next or url_for('home'))

    return render_template('auth/login.html', form=form)
