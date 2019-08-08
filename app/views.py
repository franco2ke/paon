from flask import render_template, Blueprint, url_for

main_site_bp = Blueprint('main_site', __name__)

@main_site_bp.route('/')
def index():
    return render_template('index.html')
