import argparse
import os, sys
import pickle
import numpy as np

# This try-catch is a workaround for Python3 when used with ROS; it is not needed for most platforms
try:
    sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
except:
    pass

import cv2
import imutils

import matplotlib.pyplot as plt

cap = cv2.VideoCapture('/home/rohan/Desktop/ENPM673/Project1/AR Project/Input Sequences/Tag0.mp4',0)
print(cap.isOpened())

while(True):
    ret, frame = cap.read()
    print(ret)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    edges = cv2.Canny(blur,240,250)
    cnts, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # area = [cv2.contourArea(c) for c in cnts]
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)
    # cnts = sorted(cnts, key=lambda c: cv2.arcLength(c, True), reverse=True)
    # t = 0
    # for c in cnts:
    #     perimeter = cv2.arcLength(c,True)
    #     if perimeter > t :
    #         t = perimeter
    #         max = c
    # cnts = imutils.grab_contours(np.array(cnts))
    # cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
    # screenCnt = None
    # print(len(contours))
    cv2.drawContours(gray, cnts[1], -3, (0,0,0), 4)
    # dst = cv2.cornerHarris(gray,2,3,0.04)
    # #result is dilated for marking the corners, not important
    # dst = cv2.dilate(dst,None)
    # # Threshold for an optimal value, it may vary depending on the image.
    # frame[dst>0.01*dst.max()]=[0,0,255]
    cv2.imshow('gray',np.hstack([gray]))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cap.release()
# cv2.destroyAllWindows()