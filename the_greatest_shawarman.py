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
#play_sound('00.startup.mp3')
time.sleep(1.5)
set_face('50', '50', '0')
time.sleep(1.5)
set_face('50', '50', '40')

play_sound('00.mp3')

time.sleep(2.5)
set_face('20', '50', '40')
time.sleep(2)
play_sound('01.mp3')
set_face('50', '50', '60')
time.sleep(4.5)
set_face('50', '50', '40')
play_sound('02.mp3')

set_face('50', '50', '0')
time.sleep(2.5)
set_face('50', '50', '50')
time.sleep(2.5)
play_sound('04.mp3')
time.sleep(3)

set_face('90', '50', '40')
time.sleep(2.5)

set_face('50', '50', '60')
time.sleep(1)
set_face('50', '90', '60')
time.sleep(2)
set_face('50', '50', '60')
play_sound('08.mp3')
time.sleep(1.5)
set_face('20', '20', '80')
time.sleep(0.5)
play_sound('09.mp3')
time.sleep(1.5)
set_face('50', '50', '60')
time.sleep(1)
play_sound('05.mp3')
time.sleep(4.5)
set_face('50', '50', '0')
time.sleep(1)
set_face('50', '50', '40')
time.sleep(4)
play_sound('06.mp3')
set_face('50', '50', '0')
time.sleep(1)
set_face('30', '50', '40')
time.sleep(4)
set_face('50', '50', '0')
time.sleep(1)
set_face('50', '50', '40')
time.sleep(4)

play_sound('07.mp3')

time.sleep(4)

