import zmq
import time
import serial

def start_dealing(ser, sock):
    while True:
        line = ser.readline().decode("utf-8").strip()
        values = line.split(',')
        msg = {"values": values}
        sock.send_json(msg)
        print(msg)

def dealer():
    reconnect_interval = 0.5;
    while True:
        try:
            ser = serial.Serial("/dev/ttyUSB0", 115200) 
            context = zmq.Context()
            sock = context.socket(zmq.PUSH)
            sock.connect("tcp://127.0.0.1:5559")
            start_dealing(ser, sock)
        except Exception as e:
            print(e)
        finally:
            print(time.time(), ": something happened up the stack, trying to reinitialize dealer")
            time.sleep(reconnect_interval)

dealer()
