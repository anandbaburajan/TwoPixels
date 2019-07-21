"""
Usage:
  test.py encode -i <input> -o <output> -t <text>
  test.py decode -i <input>

Options:
  -h, --help                Show this help
  -t, --text=<file>         Text to hide
  -i, --in=<input>          Input video file
  -o, --out=<output>        Resultant video file
"""

import cv2
import docopt
import numpy as np
from PIL import Image

class Video():
    def __init__(self, im):
        self.image = im
        self.width, self.height = im.size

    def encode_bit(self, bit):
        hsv_img = self.image.convert('HSV')
        pxl = hsv_img.load()
        if bit == '0':
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
        self.image = hsv_img.convert('RGB')
        if a<0:
            return '0'
        else:
            return '1'

def encode_vid(vid, result, text):
    cap = cv2.VideoCapture(vid)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter(result, fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))
    bin_text = "".join(f"{ord(k):08b}" for k in text)
    bin_text = bin_text + "0010001100100011"
    i=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        if  i!=(len(bin_text)-1):
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_frame = Video(Image.fromarray(img))
            pil_frame_en = pil_frame.encode_bit(bin_text[i])
            frame_en = cv2.cvtColor(np.array(pil_frame_en), cv2.COLOR_RGB2BGR)
            out.write(frame_en)
            i+=1
        else:
            out.write(frame)
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def decode_vid(vid):
    bin_text=""
    cap = cv2.VideoCapture(vid)
    i=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        if "0010001100100011" not in bin_text:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_frame = Video(Image.fromarray(img))
            bin_text = bin_text + pil_frame.decode_bit()
            i+=1
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    bin_text = bin_text[0:-16]
    text=''.join(chr(int(bin_text[k:k+8], 2)) for k in range(0, len(bin_text), 8))
    return text

def main():
    args = docopt.docopt(__doc__)
    input = args["--in"]
    output = args["--out"]
    text = args["--text"]

    if args["encode"]:
        encode_vid(input, output, text)
    elif args["decode"]:
        print(decode_vid(input))

if __name__=="__main__":
    main()
