from flask import render_template, redirect, url_for, request   # imports tools for pages, redirects, and forms
from app import app, db, Listing                                # imports our app, database, and Listing model

@app.route('/')                                # when someone visits the homepage
def index():                                   # run this function
    listings = Listing.query.all()             # fetch every listing from the database
    return render_template('index.html', listings=listings)     # show the homepage and pass listings to it

@app.route('/listing/<int:id>')                # when someone visits /listing/3 for example
def listing(id):                               # run this function with id=3
    listing = Listing.query.get_or_404(id)     # fetch that listing or show a 404 page if it doesn't exist
    return render_template('listing.html', listing=listing)     # show the listing detail page

@app.route('/post', methods=['GET', 'POST'])   # handles both loading the form and submitting it
def post():                                    # run this function for the post-an-item page
    if request.method == 'POST':               # if the form was submitted
        listing = Listing(
            title=request.form['title'],           # get the title the user typed
            description=request.form['description'], # get the description
            price=float(request.form['price']),    # get the price and convert it to a number
            category=request.form['category'],     # get the selected category
            email=request.form['email']            # get the seller's contact email
        )
        db.session.add(listing)                # stage the new listing to be saved
        db.session.commit()                    # save it to the database
        return redirect(url_for('index'))      # send the user back to the homepage
    return render_template('post.html')        # if just loading the page, show the empty form

