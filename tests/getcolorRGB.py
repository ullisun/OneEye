import cv2
import numpy as np

def get_dominant_color(image):
    """ Berechnet die dominante Farbe über den Median der Pixelwerte """
    small_img = cv2.resize(image, (100, 100))  # Bild verkleinern für schnellere Verarbeitung
    median_color = np.median(small_img.reshape(-1, 3), axis=0)
    return median_color.astype(int)

cap = cv2.VideoCapture(0)  
ret, frame = cap.read()  
cap.release()

if ret:
    dominant_color = get_dominant_color(frame)
    print("Erkannte Farbe RGB:", dominant_color)
