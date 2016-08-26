from PIL import Image
from black_white import *

def list_intervals_shade(num_intervals):
    lst_i = []
    a1 = float(255.00/float(num_intervals))
    lst_i.append(0)
    lst_i.append(a1)
    for i in xrange(2,num_intervals):
	    lst_i.append((i * a1))
    lst_i.append(255.0)
    return lst_i


def interval_verification(rgb,lst_intervals):
    for i in xrange(len(lst_intervals)):
        if(float(rgb)<=lst_intervals[i]):
            return ((lst_intervals[i-1] + lst_intervals[i])/2)
    
def quantitization(a_image, shades):
    new_image = Image.new("RGB",a_image.size,"black")
    pixels = new_image.load()
    xy = a_image.size
    w = xy[0]
    h = xy[1]
    
    lst_i = list_intervals_shade(shades) 

    for x in xrange(w):
        for y in xrange(h):
            rgb  = a_image.getpixel((x,y))
            if (rgb[0] == rgb[1] and rgb[1] == rgb[2]):
                l = interval_verification(rgb[0],lst_i)
                pixels[x,y] = (int(l),int(l),int(l))
    return new_image


print list_intervals_shade(2)