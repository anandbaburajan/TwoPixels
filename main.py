# USAGE
# python main.py --video vid.mp4

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
	help="Input video file")
args = vars(ap.parse_args())

cap = cv2.VideoCapture(args["video"])

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
