from PIL import Image
#=========================================
# Given a image, returns a Image with brightness
# Where: 
# Pixel = Pixel * c
# C -> Constant for brightness
# Returns a image
#=========================================
def brightness_rgb(im,a):
    new_image = Image.new("RGB",im.size,"black")
    pixels = new_image.load() #create the pixel map

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            rgb = im.getpixel((i,j))
            pixels[i,j] = (int(a * rgb[0]) , int(a * rgb[1]), int(a * rgb[2]))
    return new_image
#---------------------------------
# Tests
#---------------------------------
# im = Image.open("young-stalin.jpeg")
# nw_im = brightness_rgb(im,0.56)
# nw_im.show()