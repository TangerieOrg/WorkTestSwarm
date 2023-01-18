from flask import Flask
from flask import jsonify
import socket
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "Hostname": socket.gethostname(),
        "video": os.path.exists("/dev/video0")
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8123)