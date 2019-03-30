#!/bin/sh
python3 /home/pi/Documents/Victor/streamer_device_face.py &
python3 /home/pi/Documents/Victor/streamer_device_sounds.py &
python3 /home/pi/Documents/Victor/task_worker_face.py &
python3 /home/pi/Documents/Victor/task_worker_sounds.py &
python3 /home/pi/Documents/Victor/the_greatest_shawarman.py
