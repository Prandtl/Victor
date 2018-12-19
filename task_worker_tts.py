import time
import sys
import zmq
import random
import vlc
import urllib.parse as urlparse

def consumer():
    consumer_id = random.randrange(1, 10005)
    context = zmq.Context()
    reciever = context.socket(zmq.PULL)
    reciever.connect("tcp://127.0.0.1:5560")
    while True:
        work = reciever.recv_json()
        data = work["message"]
        message = urlparse.quote(data)
        p = vlc.MediaPlayer('https://tts.voicetech.yandex.net/tts?text=' + message)
        p.play()

consumer()
