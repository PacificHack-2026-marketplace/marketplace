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
# test case
#test case2

