import numpy as np
import cv2
from matplotlib import pyplot as plt

def zoom_i():
    im = cv2.imread('young-stalin.jpeg')
    small = cv2.resize(im, (0,0), fx=0.5, fy=0.5)
    cv2.imshow("resized", small)
    cv2.imshow("image", im)
    cv2.waitKey(0)

def zoom_o():
    im = cv2.imread('young-stalin.jpeg')
    big = cv2.resize(im, (0,0), fx=2, fy=2)
    cv2.imshow("resized", big)
    cv2.imshow("image", im)
    cv2.waitKey(0)

zoom_i()