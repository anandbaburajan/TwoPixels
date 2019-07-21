TwoPixels
=================

A Python steganography tool to hide text in videos using the HSV values of pixels.

Each frame of the carrier video stores a bit of the text using two pixels at two corners of the frame. The hidden text can be accurately extracted from the video using the difference of HSV *value* dimensions of the two pixels in each frame.

Installation
------------

```bash
pip install -r requirements.txt
```

Usage
-----

```bash
Usage:
  TwoPixels.py encode -i <input> -o <output> -t <text>
  TwoPixels.py decode -i <input>

Options:
  -h, --help                Show this help
  -t, --text=<file>         Text to hide
  -i, --in=<input>          Input video file
  -o, --out=<output>        Resultant video file
```

Import as python module
-------------

```python
#encoding
import TwoPixels as TP
TP.encode_vid("video.mp4", "result.mp4", "Hello")

#decoding
import TwoPixels as TP
print(TP.decode_vid("video.mp4"))
```
