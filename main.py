#import libraries
import cv2
import numpy as np
#import files and functions/methods
from filter import * #does all the filtering and masking
from olines import * #does the line detecting and overlay, including middle line
# Saves video feed
videoCapture = cv2.VideoCapture(0)

while True:
    # Goes through each frame to process and overlay
    ret, img = videoCapture.read()
    filtered = filter_frame(img) #filters image, more edxplanation in function definition
    masked = create_mask(filtered, 300, 100, 800, 800)
    lines = detect_lines(masked)

    if lines is not None:
        # Draws the detected lines as well as the center line
        draw_lines(img, lines)

    # Draws a rectangle to show where the mask is.
    cv2.rectangle(img, (300, 100), (1080, 900), (255, 255, 255), 3)

    # Display the frame with the lines
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
videoCapture.release()
cv2.destroyAllWindows()