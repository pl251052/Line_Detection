import cv2
import numpy as np

videoCapture = cv2.VideoCapture(0)

while (True):
    ret, img = videoCapture.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    ret, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)

    edges = cv2.Canny(thresh, 50, 150, apertureSize=3)

    x = 300
    y = 100
    w = 800
    h = 800
    mask = np.zeros(edges.shape[:2], np.uint8)
    mask[y:y + h, x:x + w] = 255
    masking = cv2.bitwise_and(edges, edges, mask=mask)

    lines = cv2.HoughLinesP(masking, rho=1, theta=np.pi / 180, threshold=100, minLineLength=50, maxLineGap=720)

    if lines is not None:
        liney = []
        for line in lines:
            x1, y1, x2, y2 = line[0]

            # Check proximity to existing lines
            close = False
            for lline in liney:
                ax, ay, bx, by = lline
                distance1 = np.sqrt((x1 - ax) ** 2 + (y1 - ay) ** 2)
                distance2 = np.sqrt((x2 - bx) ** 2 + (y2 - by) ** 2)

                if distance1 < 60 or distance2 < 60:
                    close = True
                    break

            if not close:
                liney.append([x1, y1, x2, y2])
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 4)

            if lines is not None and len(liney) >= 2:
                ax = int((liney[0][0] + liney[1][0]) / 2)
                ay = int((liney[0][1] + liney[1][1]) / 2)
                bx = int((liney[0][2] + liney[1][2]) / 2)
                by = int((liney[0][3] + liney[1][3]) / 2)

                start_point = (ax, ay)
                end_point = (bx, by)
                cv2.line(img, start_point, end_point, (0, 0, 255), 5)

        cv2.rectangle(img, (x+10, y+10), (x + w-10, y + h), (255, 255, 255), 3)

        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

videoCapture.release()
cv2.destroyAllWindows()

# CODE WORKS CITED
# Hough Lines Documentation (Lines 13-15, 25): https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html
# Masking (Lines-17-23): https://stackoverflow.com/questions/11492214/opencv-via-python-is-there-a-fast-way-to-zero-pixels-outside-a-set-of-rectangle