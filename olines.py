#import libraries
import cv2
import numpy as np
def detect_lines(masked):
    # Detects lines using Hough Transform
    return cv2.HoughLinesP(masked, rho=1, theta=np.pi / 180, threshold=100, minLineLength=50, maxLineGap=720)

def draw_lines(img, lines):
    liney = [] #will hold the values of the detected lines
    for line in lines:
        x1, y1, x2, y2 = line[0]

        # Checks if the same line is being detected twice by using distance
        close = False
        for lline in liney: #runs through each value in "liney" to compar against "lines"
            ax, ay, bx, by = lline
            #does the distance formula on each endpoint
            distance1 = np.sqrt((x1 - ax) ** 2 + (y1 - ay) ** 2)
            distance2 = np.sqrt((x2 - bx) ** 2 + (y2 - by) ** 2)

            # if the points are too close close is set equal to true
            if distance1 < 60 or distance2 < 60:
                close = True
                break

        if not close: #If close is false, meaning the lines aren't too close, the detected line is appended to the list and displayed
            liney.append([x1, y1, x2, y2])
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 4) #these lines are blue

    if len(liney) >= 2:
        # Uses list of detected lines to find the midpoint of each of the end points
        ax = int((liney[0][0] + liney[1][0]) / 2)
        ay = int((liney[0][1] + liney[1][1]) / 2)
        bx = int((liney[0][2] + liney[1][2]) / 2)
        by = int((liney[0][3] + liney[1][3]) / 2)

        # Uses those midpoints to make middle line
        start_point = (ax, ay)
        end_point = (bx, by)
        cv2.line(img, start_point, end_point, (0, 0, 255), 5) #center lines are red and slightly thicker.
