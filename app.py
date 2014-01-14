from flask import Flask, render_template
from flask import request, session, url_for
from flask.ext.scss import Scss
from flask.ext.sqlalchemy import SQLAlchemy

import base

config = base.get_config()

# Blueprints
from base.controllers.static_pages import static_pages

app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object('config')
app.register_blueprint(static_pages)

Scss(app, static_dir='static', asset_dir='assets')

if __name__ == '__main__':
    app.run()
