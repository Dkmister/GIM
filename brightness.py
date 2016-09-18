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
            sum_red = a + rgb[0]
            if sum_red < 0:
                sum_red = 0
            elif sum_red > 255:
                sum_red = 255
            sum_green = a + rgb[1]
            if sum_green < 0:
                    sum_red = 0
            elif sum_green > 255:
                sum_red = 255
            sum_blue = a + rgb[2]
            if sum_blue < 0:
                    sum_red = 0
            elif sum_blue > 255:
                sum_red = 255
            pixels[i,j] = (int(sum_red),int(sum_green),int(sum_blue))
    return new_image

#---------------------------------
# Tests
#---------------------------------
im = Image.open("young-stalin.jpeg")
im.show()
nw_im = brightness_rgb(im,-12.56)
nw_im.show()
nw_im2 = brightness_rgb(im,20)
nw_im2.show()