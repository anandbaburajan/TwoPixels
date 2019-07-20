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
        if bit == 0:
            hsv_img.putpixel((0,0), (0,0,0))
            hsv_img.putpixel((self.width-1, self.height-1), (0,0,255))
        else:
            hsv_img.putpixel((0,0), (0,0,255))
            hsv_img.putpixel((self.width-1, self.height-1), (0,0,0))
        self = hsv_img.convert('RGB')
        return self
