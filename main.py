from flask import Flask, request, redirect, render_template, session
from db import init_db, insert_listing, Listing, get_listing, get_top_listings
from authlib.integrations.flask_client import OAuth
import dotenv
import os

dotenv.load_dotenv()


app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

oauth = OAuth(app)

google = oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_OAUTH_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_OAUTH_CLIENT_SECRET"),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

@app.route('/api/listing', methods=['POST'])
def listing_endpoint():
    user = session.get('user')

    listing = Listing(
        title=request.form.get("title"),
        category=request.form.get("category"),
        price=float(request.form.get("price")),
        contact_email=user['email'],
        user_name=user['name'],
        location=request.form.get("location"),
        description=request.form.get("description"),
    )
    id = insert_listing(listing)

    return redirect("/listing/%i" % id, 302)

@app.route('/listing/<int:id>')
def listing_view(id):
    listing = get_listing(id)
    print(listing)
    return render_template("listing.html", listing=listing)

@app.route('/')
def base():
    search_params = {}
    if 'category' in request.args:
        search_params['category'] = request.args.get('category')

    if 'q' in request.args:
        search_params['search_keywords'] = request.args.get('q').split(' ')

    listings = get_top_listings(**search_params)
    return render_template("index.html", listings=listings)

@app.route('/listing/create')
def create_listing():
    user = session.get('user')

    if user is None:
        return redirect("/login", 302)

    print(user)
    return render_template("create_listing.html", user=user)

@app.route('/login')
def login():
    return google.authorize_redirect(redirect_uri='http://127.0.0.1:5000/api/oauth/callback')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/', 302)

@app.route('/api/oauth/callback')
def callback():
    token = google.authorize_access_token()
    user = token.get("userinfo")    # insecure btw

    # user info
    session['user'] = user

    return redirect('/listing/create')

"""
@app.route('/base')
def base():
    return render_template("base.html")
    
@app.route('/index') 
def index():
    return render_template("index.html", message="hello world")

@app.route('/listing')
def listing():
    return render_template("listing.html")
    
"""

if __name__ == '__main__':
    init_db()
    app.run()
