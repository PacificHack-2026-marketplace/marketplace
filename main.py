from flask import Flask

app = Flask(__name__)

@app.route('/api/helloworld', methods=['GET'])
def send():
    return "hello world", 200

if __name__ == '__main__':
    app.run()
