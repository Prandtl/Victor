import time
import sys
import zmq
import random
import pygame
import urllib.parse as urlparse

def consumer():
    consumer_id = random.randrange(1, 10005)
    context = zmq.Context()
    reciever = context.socket(zmq.PULL)
    reciever.connect("tcp://127.0.0.1:5566")
    pygame.mixer.init()
    while True:
        try:
            work = reciever.recv_json()
            path = work["fileName"]
            pygame.mixer.music.load("./sounds/" + path)
            pygame.mixer.music.play()

        except Exception as e:
            print("SOUNDS", e)
            context = zmq.Context()
            reciever = context.socket(zmq.PULL)
            reciever.connect("tcp://127.0.0.1:5566")

consumer()
