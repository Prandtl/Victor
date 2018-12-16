import time
import sys
import zmq
import random

def consumer():
    consumer_id = random.randrange(1, 10005)
    print("I am consumer #" + str(consumer_id))
    context = zmq.Context()
    reciever = context.socket(zmq.PULL)
    reciever.connect("tcp://127.0.0.1:5560")
    while True:
        work = reciever.recv_json()
        data = work["values"]
        result = {"consumer": consumer_id, "values": data}
        print(result)

consumer()
