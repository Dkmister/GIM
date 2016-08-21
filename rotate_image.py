from PIL import Image

#===============================
#   Given a image, return a Image matrix with
#   Inverted values of the original one
#===============================
def rotate_image(a_image):
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

im = Image.open("young-stalin.jpeg")
nw_im = rotate_image(im)
nw_im.show()

