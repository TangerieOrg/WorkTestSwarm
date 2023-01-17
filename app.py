from flask import Flask
from flask import jsonify
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(f'App {socket.gethostname()}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8123)