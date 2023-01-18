from flask import Flask, Response
from flask import jsonify
import socket
import os
import cv2

app = Flask(__name__)

video = cv2.VideoCapture(0)


def gen(video):
        success, image = video.read()

        ret, jpeg = cv2.imencode('.jpg', image)

        frame = jpeg.tobytes()

        return (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/')
def index():
    return jsonify({
        "Hostname": socket.gethostname(),
        "video": os.path.exists("/dev/video0")
    })


@app.route('/video')
def video_feed():
    # Set to global because we refer the video variable on global scope,
    # Or in other words outside the function
    global video

    # Return the result on the web
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8123)