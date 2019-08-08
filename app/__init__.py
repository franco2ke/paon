import os
from flask import Flask
from config import app_config

config_name = os.getenv('FLASK_ENV')

app = Flask(__name__)
app.config.from_object(app_config[config_name])
app.url_map.strict_slashes = False

from app.views import main_site_bp
app.register_blueprint(main_site_bp)



