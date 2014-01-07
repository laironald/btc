from flask import Blueprint, render_template

static_pages = Blueprint('static_pages', __name__)
controller = "static_pages"

# --- login callback ---
@static_pages.route('/')
def index():
    method = "index"
    return render_template('views/index.html', method=method, controller=controller)
