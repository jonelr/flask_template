# myapp/site/__init__.py

from flask import Blueprint

site_bp = Blueprint("site_bp", __name__,
                    template_folder='templates', static_folder='static')
