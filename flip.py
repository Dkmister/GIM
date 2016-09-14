from PIL import Image



#===============================
#   Given a image, return a Image flipped image
#   Use the principle of turning the first element of a matrix 
#   Into the last one of the same line
#===============================

def flip(a_image):
    new_image = Image.new("RGB",a_image.size,"black")
    pixels_new = new_image.load()
    pixels_old = a_image.load()
    xy = a_image.size
    w = xy[0]
    h = xy[1]
    
    for i in xrange(w):
        for j in xrange(h):
            rgb = a_image.getpixel((i,j))
            pixels_new[w-i-1,j] = (rgb[0],rgb[1],rgb[2])
    return new_image



#-------------------
# Tests using Stalin
#-------------------
im = Image.open("young-stalin.jpeg")
im.show()
nw_im = flip(im)
nw_im.show()
