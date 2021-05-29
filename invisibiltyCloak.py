import cv2
import numpy as np
import pygame
from pygame import mixer

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
back = cv2.imread('./image.jpg')
pygame.init()
mixer.music.load("song.mp3")
mixer.music.play(-1)
while cap.isOpened():
   
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        l_red = np.array([0, 100, 100])
        u_red = np.array([10, 255, 255])
        mask = cv2.inRange(hsv, l_red, u_red)
        part1 = cv2.bitwise_and(back, back, mask=mask)
        mask = cv2.bitwise_not(mask)
        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('final', part1 + part2)
        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()