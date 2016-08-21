from PIL import Image
#===============================
#   Given a image, return a Image rotated 90 degrees
#   Use the principle of inverting the y and turning into the x
#   Also create a image with the width and height inverted
#===============================

def rotate_image_90(a_image):
    xy = a_image.size
    w = xy[0]
    h = xy[1]
    new_image = Image.new("RGB",(h,w),"black")
    pixels_new = new_image.load()
    pixels_old = a_image.load()
    
    for i in xrange(w):
        for j in xrange(h):
            rgb = a_image.getpixel((i,j))
            pixels_new[h-j-1,w-i-1] = (rgb[0],rgb[1],rgb[2])
    return new_image
#-----------------------------------
# Test using a simple image of Stalin 
# Status = OK
#-----------------------------------
im = Image.open("young-stalin.jpeg")
im.show()
nw_im = rotate_image_90(im)
nw_im.show()