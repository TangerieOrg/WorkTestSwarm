from flask import Flask, Response
from flask import jsonify
import socket
import os
import cv2
import grp
import pwd

app = Flask(__name__)

video = cv2.VideoCapture(0)


def gen(video):
        success, image = video.read()

        ret, jpeg = cv2.imencode('.jpg', image)

        frame = jpeg.tobytes()

        return (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def get_cameras():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

def file_perms(path):
    return {x: os.access(os.path.join(path, x), os.R_OK) for x in os.listdir(path)}

@app.route('/')
def index():
    return jsonify({
        "Hostname": socket.gethostname(),
        "video": os.path.exists("/dev/my-video0"),
        "cameras": get_cameras(),
        "groups": [grp.getgrgid(x).gr_name for x in os.getgroups()],
        "user": pwd.getpwuid(os.getuid())[0],
        "/dev": file_perms("/dev")
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