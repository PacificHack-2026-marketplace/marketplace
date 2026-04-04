from flask import Flask, request, redirect, render_template
from db import init_db, insert_listing, Listing, get_listing

app = Flask(__name__)

@app.route('/api/listing', methods=['POST'])
def listing_endpoint():
    listing = Listing(
        title=request.form.get("title"),
        category=request.form.get("category"),
        price=float(request.form.get("price")),
        user_name=request.form.get("user_name"),
        contact_email=request.form.get("contact_email"),
        contact_phone=request.form.get("contact_phone"),
        location=request.form.get("location"),
        description=request.form.get("description"),
        summary=request.form.get("summary"),
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
    return render_template("index.html")

@app.route('/listing/create')
def create_listing():
    return render_template("create_listing.html")

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
    
@app.route('/debug')
def debug():
    return render_template("debug.html")
"""

if __name__ == '__main__':
    init_db()
    app.run()
