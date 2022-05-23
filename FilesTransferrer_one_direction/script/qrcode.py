import pyqrcode
# import sys
import io
import os
from PIL import Image

def qrcode(url):
    location = "QRCode/WebQRCode.png"

    url = pyqrcode.create(url)

    with open(location, 'wb') as fstream:
        url.png(fstream, scale=9)

    # same as above
    url.png(location, scale=9)

    # in-memory stream is also supported
    buffer = io.BytesIO()
    url.png(buffer)

    img = Image.open(location)
    img.show() 

if __name__ == "__main__":

    qrcode("http://192.168.1.104")

    pass