import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from black_white import *

def histogram_list(a_image):
    
    hist_lst = []

    for element in range(256):
        hist_lst.append(0)

    for i in range(a_image.size[0]):
        for j in range(a_image.size[1]):
            rgb = a_image.getpixel((i,j))
            if(rgb[0]==rgb[1] and rgb[1]==rgb[2]):
                hist_lst[rgb[0]] += 1



    return hist_lst
#-------------------------------
# Tests following the image
#-------------------------------
# im = Image.open("young-stalin.jpeg")
# nw_im = black_white(im)
# lst = histogram_list(nw_im)
# print lst , len(lst)
                
