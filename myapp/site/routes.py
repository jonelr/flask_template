# myapp/site/routes.py

from myapp.site import site_bp
from flask import render_template, redirect


@site_bp.route('/', methods=['GET'])
def home():
    return render_template('site/index.html')
