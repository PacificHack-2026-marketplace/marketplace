from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/api/helloworld', methods=['GET'])
def send():
    return "hello world", 200

@app.route('/')
def index():
    return render_template("index.html", message="hello world")


if __name__ == '__main__':
    app.run()
    url_for('static', filename='style.css')

