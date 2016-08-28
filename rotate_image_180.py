from PIL import Image

#===============================
#   Given a image, return a Image rotated 180 degrees
#   Use the principle of turning the first element of a matrix 
#   Into the last one
#===============================
def rotate_image_180(a_image):
    new_image = Image.new("RGB",a_image.size,"black")
    pixels_new = new_image.load()
    pixels_old = a_image.load()
    xy = a_image.size
    w = xy[0]
    h = xy[1]
    
    for i in xrange(w):
        for j in xrange(h):
            rgb = a_image.getpixel((i,j))
            pixels_new[w-i-1,h-j-1] = (rgb[0],rgb[1],rgb[2])
    return new_image
#-----------------------------------
# Test using a simple image of Stalin 
# Status = OK
#-----------------------------------
# im = Image.open("young-stalin.jpeg")
# im.show()
# nw_im = rotate_image_180(im)
# nw_im.show()
# nw_im = rotate_image_180(nw_im)
# nw_im.show()
