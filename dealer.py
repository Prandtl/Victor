import zmq
import time

def start_dealing(sock_tts, sock_face):
    while True:
        inp = input().strip()
        vals = inp.split(' ')
        if(vals[0]=='T'):
            msg = {"message": ' '.join(vals[1:])}
            sock_tts.send_json(msg)
            print(msg)
        if(vals[0]=='F'):
            msg = {'x': vals[1], 'y': vals[2], 'e': vals[3]}
            sock_face.send_json(msg)
            print(msg)

def dealer():
    reconnect_interval = 0.5;
    while True:
        try: 
            context = zmq.Context()
            sock_tts = context.socket(zmq.PUSH)
            sock_tts.connect("tcp://127.0.0.1:5559")
            context2 = zmq.Context()
            sock_face = context.socket(zmq.PUSH)
            sock_face.connect("tcp://127.0.0.1:65000")
            start_dealing(sock_tts, sock_face)
        except Exception as e:
            print(e)
        finally:
            print(time.time(), ": something happened up the stack, trying to reinitialize dealer")
            time.sleep(reconnect_interval)

dealer()
