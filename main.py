# USAGE
# python main.py -i vid.mp4 -v wbSwFU6tY1c
# Result video => en_vid.mp4

from VideoID import *
import numpy as np
import argparse
import cv2
from PIL import Image

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="Input video file")
    ap.add_argument("-v", "--videoid", required=True, help="11 byte Video ID")
    args = vars(ap.parse_args())

    cap = cv2.VideoCapture(args["input"])

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter("en_" + args["input"],fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()
