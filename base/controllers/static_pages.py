from flask import Blueprint, render_template
from base.forms import LoginForm

static_pages = Blueprint('static_pages', __name__)
controller = "static_pages"

# --- login callback ---
@static_pages.route('/')
def index():
    method = "index"
    return render_template('views/index.html', method=method, controller=controller)

@static_pages.route('/index_user.html')
def index_user():
    method = "index_user"
    loginform = LoginForm()
    return render_template('views/index_user.html', method=method, controller=controller, form=loginform)

@static_pages.route('/<page>')
def index_page(page):
    method = page
    return render_template('views/{0}'.format(page), method=method, controller=controller)
