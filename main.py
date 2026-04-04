from flask import Flask, url_for, render_template
import sqlite3

db = sqlite3.connect("database.db")
app = Flask(__name__)

@app.route('/api/helloworld', methods=['GET'])
def send():
    return "hello world", 200

@app.route('/')
def index():
    return render_template("index.html", message="hello world")


def init_db():
    cur = db.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS listing(
        listing_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT
    );
    """)
    cur.close()


if __name__ == '__main__':
    init_db()
    app.run()
# test case
#test case2
