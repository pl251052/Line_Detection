#Sources:
#Hough Line Transform Tutorial - https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html
#Masking - https://stackoverflow.com/questions/11492214/opencv-via-python-is-there-a-fast-way-to-zero-pixels-outside-a-set-of-rectangle
#Hough Line Transform Tutorial - used for lines 6-10 of filter.py and line 6 of olines.py
#Masking - used for lines 12-16 in filter.py


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