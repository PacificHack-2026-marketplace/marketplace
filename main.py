from flask import Flask, request, redirect, render_template
from db import init_db, insert_listing, Listing, get_listing

app = Flask(__name__)

@app.route('/api/listing', methods=['POST'])
def listing_endpoint():
    listing = Listing(
        title=request.form.get("title"),
        price=float(request.form.get("price")),
        user_name=request.form.get("user_name"),
        contact_email=request.form.get("contact_email"),
        contact_phone=request.form.get("contact_phone"),
        location=request.form.get("location"),
        description=request.form.get("description"),
        summary=request.form.get("summary"),
    )
    insert_listing(listing)

    # TODO: redirect to listing page
    return redirect("/", 302)

@app.route('/listing/<int:id>')
def listing_view(id):
    listing = get_listing(id)
    print(listing)
    return render_template("listing.html", listing=listing)


@app.route('/') # the website itself
def index():
    return render_template("base.html", message="hello world")




@app.route('/debug')
def debug():
    return render_template("debug.html")


if __name__ == '__main__':
    init_db()
    app.run()



#Main updated file (might not use)

from flask import Flask                        # imports Flask to create our web app

app = Flask(__name__)                          # creates the Flask app
app.config['SECRET_KEY'] = 'abc123'           # a simple secret key (fine for a hackathon)

from routes.py import *                           # loads all our page routes from routes.py

if __name__ == '__main__':                     # only runs when we start the app directly
    with app.app_context():                    # gives Flask the context it needs to access the database
        db.create_all()                        # creates the database tables if they don't exist yet
    app.run(debug=True)                        # starts the local server at http://localhost:5000
