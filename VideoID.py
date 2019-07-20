import cv2
import docopt
import numpy as np
from PIL import Image

class VideoID():
    def __init__(self, im):
        self.image = im
        self.width, self.height = im.size
