# myapp/site/routes.py

from flask import Blueprint, redirect, render_template

site_bp = Blueprint("site_bp", __name__,
                    template_folder='templates', static_folder='static')


@site_bp.route('/')
def home():
    return render_template('site/index.html')
