import zmq
import time

context = zmq.Context()
sock_sounds = context.socket(zmq.PUSH)
sock_sounds.connect('tcp://127.0.0.1:5565')
context2 = zmq.Context()
sock_face = context.socket(zmq.PUSH)
sock_face.connect('tcp://127.0.0.1:65000')

def play_sound(filename):
    msg = {'fileName': filename}
    sock_sounds.send_json(msg)

def set_face(x, y, e):
    msg = {'x': x, 'y':y, 'e': e}
    sock_face.send_json(msg)

set_face('50', '50', '40')
play_sound('00.startup.mp3')
time.sleep(1.5)
set_face('50', '50', '0')
time.sleep(1.5)
set_face('50', '50', '40')

play_sound('01.zahar_hello.ogg')


