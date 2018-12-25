#!/bin/env/python3
import zmq
import sys
import time
import bottle
import json
from bottle import request, response
from bottle import post, get, put, delete

DEBUG = True

app = application = bottle.default_app()

context = zmq.Context()
sock_sounds = context.socket(zmq.PUSH)
sock_sounds.connect("tcp://127.0.0.1:5565")
context2 = zmq.Context()
sock_face = context.socket(zmq.PUSH)
sock_face.connect("tcp://127.0.0.1:65000")

@post('/face')
def process_face_action():
    global DEBUG
    try:
        try:
            data = request.json
        except:
            raise ValueError

        if not DEBUG:
            try:
                sock_face.send_json(data)
            except:
                raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 500
        return
    response.headers['Content-Type'] = 'application/json'
    return data

@post('/tts')
def process_sounds_action():
    global DEBUG
    try:
        try:
            data = request.json
        except:
            raise ValueError

        if not DEBUG:
            try:
                sock_sounds.send_json(data)
            except:
                raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 500
        return
    response.headers['Content-Type'] = 'application/json'
    return data

@post('/scripts')
def process_script():
    global DEBUG
    try:
        try:
            data = request.json
        except:
            raise ValueError

        if not DEBUG:
            try:
                for d in data:
                    print(d)
                    if d["type"] == "face":
                        sock_face.send_json(d["payload"])
                    elif d["type"] == "voice":
                        sock_sounds.send_json(d["payload"])
                    time.sleep(0.5)
                    # sock_tts.send_json(data)
            except Exception as e:
                raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 500
        return
    response.headers['Content-Type'] = 'application/json'
    return
    
    try:
        try:
            data = request.json
        except:
            raise ValueError

        if not DEBUG:
            try:
                sock_sounds.send_json(data)
            except:
                raise KeyError
 
@post('/turnon')
def process_turnon():
    global DEBUG
    try:
        try:
            data = request.json
        except:
            raise ValueError

        if not DEBUG:
            try:
                sock_sounds.send_json({"fileName":"startup.mp3"})
            except:
                raise KeyError


    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 500
        return
    response.headers['Content-Type'] = 'application/json'
    return

@post('/turnoff')
def process_turnon():
    global DEBUG
    try:
        if not DEBUG:
            try:
                pass
            except Exception as e:
                raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 500
        return
    response.headers['Content-Type'] = 'application/json'
    return


if __name__ == '__main__':
    DEBUG = len(sys.argv) > 1
    #print(f"DEBUG mode is ${DEBUG}")
    bottle.run(host='0.0.0.0', port=31337)

