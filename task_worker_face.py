import time
import sys
import zmq
import random
import vlc
import urllib.parse as urlparse
import serial

def consumer():
    ser = serial.Serial('/dev/ttyUSB0', 115200)
    consumer_id = random.randrange(1, 10005)
    context = zmq.Context()
    reciever = context.socket(zmq.PULL)
    reciever.connect("tcp://127.0.0.1:65001")
    while True:
        try:
            print('waiting...', file=open("/home/pi/Documents/Victor/face.log", "a"))
            work = reciever.recv_json()
            print(work, file=open("/home/pi/Documents/Victor/face.log", "a"))
            x = work["x"]
            y = work["y"]
            e = work["e"]
            conf = ('LX'+x+'RX'+x+'LY'+y+'RY'+str(100-int(y))+'E'+e)
            ser.write(conf.encode('utf-8'))
        except Exception as e:
            print("FACE", e, file=open("/home/pi/Documents/Victor/face.log", "a"))
            ser = serial.Serial('/dev/ttyUSB0', 115200)
            consumer_id = random.randrange(1, 10005)
            context = zmq.Context()
            reciever = context.socket(zmq.PULL)
            reciever.connect("tcp://127.0.0.1:65001")
        

consumer()
