import numpy as np
import cv2


def get_bird_location(img):
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    img = img[0:600, 170:250]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    lower_red = np.array([200, 70, 60])
    upper_red = np.array([255, 110, 100])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    points = cv2.findNonZero(mask)
    avg = (170, 50)

    if points is not None:
        avg = np.mean(points, axis=0)
        avg = avg[0]

    return (int(avg[0]) + 170, int(avg[1]))