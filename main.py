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

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">                     <!-- ensures special characters display correctly -->
    <meta name="viewport" content="width=device-width, initial-scale=1">  <!-- makes it mobile friendly -->
    <title>UniMarket</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">  <!-- loads our CSS file -->
</head>
<body>

<nav>                                          <!-- top navigation bar shown on every page -->
    <a href="/" class="logo">🎓 UniMarket</a>  <!-- clicking the logo always goes home -->
    <a href="/post" class="btn-post">+ Post Item</a>  <!-- button to post a new listing -->
</nav>

<main>
    {% block content %}{% endblock %}          <!-- each page's unique content goes here -->
</main>

</body>
</html>