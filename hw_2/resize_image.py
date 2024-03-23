import numpy as np
import cv2, os


class image:
    def __init__(self, name):
        if os.path.isfile(name):
            self.data = cv2.imread(name)
            self.data = cv2.cvtColor(self.data, cv2.COLOR_BGR2RGB)
            self.h, self.w, self.c = self.data.shape
        else:
            print('file error')



def nn_interpolate(im, c, h, w):
    height, width, channels = im.data.shape
    resized_im = np.zeros((h, w, c), dtype=im.data.dtype)
    row_ratio = height / h
    col_ratio = width / w

    for i in range(h):
        for j in range(w):
            # Find the x and y coordinates of the nearest neighbor in the input image
            y = int(round(i * row_ratio))
            x = int(round(j * col_ratio))

            # Make sure we don't go out of bounds
            y = min(y, height - 1)
            x = min(x, width - 1)
            resized_im[i, j, :] = im.data[y, x, :]
            
    return resized_im
    


def nn_resize(im, h, w):
    resized_data = nn_interpolate(im, im.c, h, w)
    height, width, channels = im.data.shape
    resized_im = np.zeros((h, w, channels), dtype=im.data.dtype)
    for i in range(h):
        for j in range(w):
            for k in range(im.c):
                resized_im[i, j, k] = resized_data[i, j, k]
    image_bgr = cv2.cvtColor(resized_im, cv2.COLOR_RGB2BGR)
    cv2.imshow("Image", image_bgr)
    cv2.waitKey(0)
    
    
    
 
def bilinear_interpolate(im, c, h, w):
    # TODO
    return 0

def bilinear_resize(im, h, w):
    # TODO
    return 0

img = image("test.png")
nn_resize(img,img.h*4,img.w*4)
