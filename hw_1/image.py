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
        i = max(0, min(i, self.h - 1))
        j = max(0, min(j, self.w - 1))
        return self.data[i, j, c]

    def set_pixel(self, i, j, c, value):
        print()
        if i < 0 or i >= self.h or j < 0 or j >= self.w:
            return
        self.data[i, j, c] = value


    def copy_image(self):
        copy_img = image("copy.png")
        copy_img.h, copy_img.w, copy_img.c = self.h, self.w, self.c
        copy_img.data = np.zeros((self.h, self.w, self.c), dtype=self.data.dtype)
        
        for i in range(self.h):
            for j in range(self.w):
                for k in range(self.c):
                    value = self.get_pixel(i, j, k)
                    copy_img.set_pixel(i, j, k, value)
                    
        img.save_image("copy_image.png", copy_img.data)
        
        return copy_img
                

    def rgb_to_grayscale(self):
        gray_img = image("gray.png")
        gray_img.h, gray_img.w, gray_img.c = self.h, self.w, 1
        gray_img.data = np.zeros((self.h, self.w,1), dtype=np.uint8)  # Single-channel, 8-bit
    
        for i in range(self.h):
            for j in range(self.w):
                # Ensure the use of BGR order if using OpenCV's default format
                blue = self.get_pixel(i, j, 0)
                green = self.get_pixel(i, j, 1)
                red = self.get_pixel(i, j, 2)
                value = int(0.299 * red + 0.587 * green + 0.114 * blue)
                gray_img.set_pixel(i, j, 0, value)  
        img.save_image("graybar.png", gray_img.data)
            # fill

    def shift_image(self, c, v):
        for i in range(self.h):
            for j in range(self.w):
                value = self.get_pixel(i, j, c)
                new_value = int(value + value*v)
                img.set_pixel(i, j, c, new_value)
         
       

    def clamp_image(self):
        for i in range(self.h):
            for j in range(self.w):
               for c in range(self.c):
                   # Get the current pixel's value for the specified channel
                pixel_value = self.get_pixel(i, j, c)
                # Clamp the value to be within [0, 1]
                clamped_value = max(0, min(1, pixel_value/256))
                # Set the pixel's clamped value for the specified channel
                self.set_pixel(i, j, c, clamped_value*256)
                   
    def hsv_to_rgb(self):
        print()

# img object
img = image('test.png')
for i in range(img.h):
    for j in range(img.w):
       for c in range(img.c):
           value = img.get_pixel(i, j, c)
           if value>255:
               print(value)

img.shift_image( 0, 0.4)
img.shift_image( 1, 0.4)
img.shift_image( 2, 0.4)
img.save_image("overflow.png", img.data)
img.clamp_image()
img.save_image("fixed.png", img.data)
#Step-1
x = 0; y = 0; c =0; value = 0

img.get_pixel(x, y, c)
img.set_pixel(x, y, c, value)
# 1. Getting and setting pixels
for row in range(img.h):
    for col in range(img.w):
        img.set_pixel(row, col,2, 0)
img.save_image("out-3.png", img.data)
img.copy_image()
img.rgb_to_grayscale()

#Step-2 etc.
# 3. Grayscale image
graybar = img.rgb_to_grayscale()
img.save_image(graybar, "graybar")

