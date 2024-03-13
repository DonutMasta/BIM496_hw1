import numpy as np
import cv2, os

class image:
    def __init__(self, name):
        if os.path.isfile(name):
            self.data = cv2.imread(name)
            self.h, self.w, self.c = self.data.shape
        else:
            print('file error')

    def save_image(self, name, data):
        cv2.imwrite(name, data)
    
    def get_pixel(self, i,j,c):
        print()
        # fill

    def set_pixel(self, i, j, c, value):
        print()
        # fill

    def copy_image(self):
        print()
        # fill
        #return copy_image

    def rgb_to_grayscale(self):
        print()
        # fill

    def shift_image(self, c, v):
        print()
        # fill

    def clamp_image(self):
        print()

    def hsv_to_rgb(self):
        print()

# img object
img = image('test.png')

#Step-1
x = 0; y = 0; c =0; value = 0
img.get_pixel(x, y, c)
img.set_pixel(x, y, c, value)
# 1. Getting and setting pixels
for row in range(im.h):
    for col in range(im.w):
        img.set_pixel(im, 0, row, col, 0)
img.save_image(im, "out-1")
#Step-2 etc.
# 3. Grayscale image
graybar = img.rgb_to_grayscale()
img.save_image(graybar, "graybar")

