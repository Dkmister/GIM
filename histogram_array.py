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

def show_bw_histogram(a_image):
    xy = a_image.size
    im_siz = xy[0]*xy[1]
    alpha_b = []
    for i in xrange(0,256):
        alpha_b.append(i)
    pos = np.arange(len(alpha_b))
    width = 1.0

    bw_im = black_white(a_image)
    lst = histogram_list(bw_im)

    ax = plt.axes()
    ax.set_xticks(pos + (width / 2))
    ax.set_xticklabels(alpha_b)

    plt.bar(pos,lst,width,color='black')
    plt.show()

   
    

#-----------------
# Tests following the image
#-------------------------------
im = Image.open("young-stalin.jpeg")
#nw_im = black_white(im)
#lst = histogram_list(nw_im)
#print lst , len(lst)
show_bw_histogram(im)
            
