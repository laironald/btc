from flask import Flask, render_template
from flask import request, session
from flask.ext.scss import Scss

import base
config = base.get_config()

# Blueprints
from base.controllers.static_pages import static_pages

app = Flask(__name__, static_folder='static', static_url_path='')
app.register_blueprint(static_pages)
app.debug = True
app.secret_key = config.get("global").get("secret")

Scss(app, static_dir='static', asset_dir='assets')

# url_for('static', filename='all.css')


# @app.route('/')
# def index():
#     '''Initialize a session for the current user, and render welcome.html.'''
#     '''Show log-in botton if user hasn't logged in.'''
#     # Create a state token.
#     state = ''.join(random.choice(string.ascii_uppercase + string.digits)
#                     for x in xrange(32))
#     session['state'] = state
#     return render_template('welcome.html', STATE = state, CLIENT_ID=CLIENT_ID)



# # --- login callback ---
# @app.route('/auth', methods=['POST','GET'])
# def callback_handler():
#     # Ensure that the request is not a forgery and that the user sending
#     # this connect request is the expected user.
#     if request.args.get('state', '') != session['state']:
#         response = make_response(json.dumps('Invalid state parameter.'), 401)
#         response.headers['Content-Type'] = 'applicatoin/json'
#         return response

#     oauth_code = request.args.get('code', '')

#     try:
#         flow = flow_from_clientsecrets('client_secrets.json', scope='')
#         flow.redirect_uri = 'postmessage'
#         credentials = flow.step2_exchange(oauth_code)
#         cred = pickle.dumps(credentials) # store the credentials for offline access
#     except FlowExchangeError:
#         response = make_response(
#             json.dumps('Failed to upgrade the authorization code.'),401)
#         response.headers['Content-Type'] = 'application/json'
#         return response

#     google_username = credentials.id_token['email'].split('@')[0] # google account of the current user
#     print "[debug] google user: " + google_username + "@gmail.com has logged in!"
#     user = di.find_google_user(google_username)
#     if user: # if user has registered in GhostDocs
#         user_handle = user.handle
#         user.credentials = cred # update credentials
#         print "[debug] this google user has already registered as " + user_handle
#     else: # if user hasn't registered, create a GhostDocs account. TODO let user choose their username, etc instead of user google username directly.
#         user_handle = google_username
#         di.create_user(google_username,
#                         google_username,
#                         user_handle,
#                         cred)

#     print 'logged in as: ' + user_handle 
#     http = httplib2.Http()
#     http = credentials.authorize(http)

#     # associate the current session with this user
#     session['user'] = user_handle

#     return redirect('/in/'+user_handle)



if __name__ == '__main__':
    app.run()