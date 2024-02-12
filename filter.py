#import libraries
import cv2
import numpy as np
def filter_frame(frame):
    # Converts the frame to grayscale, then blurs it, uses threshold and finally uses canny edge to detect edges
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    ret, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)
    edges = cv2.Canny(thresh, 50, 150, apertureSize=3)
    return edges

def create_mask(edges, x, y, w, h):
    # Creates a mask starting at (x,y) (remember the y coordinates work opposite the coordinate grid) with width w and height h.
    mask = np.zeros(edges.shape[:2], np.uint8)
    mask[y:y + h, x:x + w] = 255
    return cv2.bitwise_and(edges, edges, mask=mask)