from PIL import Image
#=============================================
# Returns a negative image of a RGB or L Image
# Where 
# Pixel = 255 - Pixel
# Returns a Image
#=============================================
def negative(im):
    new_image = Image.new("RGB",im.size,"black")
    pixels = new_image.load() #create the pixel map

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            rgb = im.getpixel((i,j))
            pixels[i,j] = (255 - rgb[0] , 255 - rgb[1], 255 - rgb[2])
    return new_image


#-------------------------------------------
# Tests
#-------------------------------------------
im = Image.open("young-stalin.jpeg")
im.show()
nw_im = negative(im)
nw_im.show()