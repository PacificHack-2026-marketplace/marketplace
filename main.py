
from flask import Flask, url_for, render_template

from db import init_db, insert_listing, Listing

app = Flask(__name__)

@app.route('/api/helloworld', methods=['GET'])
def send():
    return "hello world", 200

@app.route('/') # the website itself
def index():
    return render_template("base.html", message="hello world")






if __name__ == '__main__':
    init_db()

    listing = Listing(
        "test listing",
        420.69,
        "bob smith",
        "example@u.pacific.edu",
        18004206969,
        "The Grove",
        "testing 123\nthis is a listing description",
        "short one-liner to show in search/listings"
    )
    insert_listing(listing)

    app.run()



#Main updated file

from flask import Flask                        # imports Flask to create our web app

app = Flask(__name__)                          # creates the Flask app
app.config['SECRET_KEY'] = 'abc123'           # a simple secret key (fine for a hackathon)

from routes.py import *                           # loads all our page routes from routes.py

if __name__ == '__main__':                     # only runs when we start the app directly
    with app.app_context():                    # gives Flask the context it needs to access the database
        db.create_all()                        # creates the database tables if they don't exist yet
    app.run(debug=True)                        # starts the local server at http://localhost:5000
