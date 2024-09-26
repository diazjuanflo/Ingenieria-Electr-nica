import cv2
import imagezmq
import time

sender = imagezmq.ImageSender(connect_to='tcp://*:5555')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    sender.send_image(frame)
    time.sleep(0.1)
