# myapp/auth/routes.py

from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from myapp.auth.extensions import bcrypt, login_manager
from myapp.forms import LoginForm
from myapp.models import User, db

auth_bp = Blueprint("auth_bp", __name__,
                    template_folder='templates', static_folder='static')


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


@auth_bp.route('/logout', methods=['GET'])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template('auth/logout.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.get(User, form.email.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user)

                next = request.args.get('next')

                return redirect(next or url_for('home'))

    return render_template('auth/login.html', form=form)
