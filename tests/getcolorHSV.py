import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

if ret:
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dominant_color_hsv = np.median(hsv_image.reshape(-1, 3), axis=0).astype(int)
    
    print("Dominante Farbe in HSV:", dominant_color_hsv)

