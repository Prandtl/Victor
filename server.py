#!/bin/env/python3
import zmq
import time
import bottle
from bottle import request, response
from bottle import post, get, put, delete

app = application = bottle.default_app()

context = zmq.Context()
sock_tts = context.socket(zmq.PUSH)
sock_tts.connect("tcp://127.0.0.1:5559")
context2 = zmq.Context()
sock_face = context.socket(zmq.PUSH)
sock_face.connect("tcp://127.0.0.1:65000")

@post('/face')
def process_face_action():
    try:
        try:
            data = request.json()
            sock_face.send_json(data)
        except:
            raise ValueError
    except ValueError:
        response.status = 400
        return
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(data)

@post('/tts')
def process_tts_action():
    try:
        try:
            data = request.json()
            sock_tts.send_json(data)
        except:
            raise ValueError
    except ValueError:
        response.status = 400
        return
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(data)


if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port=31337)

