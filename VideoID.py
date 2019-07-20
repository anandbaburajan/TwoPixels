import cv2
import docopt
import numpy as np
from PIL import Image

class VideoID():
    def __init__(self, im):
        self.image = im
        self.width, self.height = im.size

    def encode_bit(self, bit):
        hsv_img = self.image.convert('HSV')
        pxl = hsv_img.load()
        if bit == 0:
            pxl[0,0] = (0,0,0)
            pxl[self.width-1, self.height-1] = (0,0,255)
        else:
            pxl[0,0] = (0,0,255)
            pxl[self.width-1, self.height-1] = (0,0,0)
        self.image = hsv_img.convert('RGB')
        return self.image

    def decode_bit(self):
        hsv_img = self.image.convert('HSV')
        pxl = hsv_img.load()
        a = pxl[0,0][2] - pxl[self.width-1, self.height-1][2]
        if a<0:
            return 0
        else:
            return 1
