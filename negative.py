from PIL import Image

def negative(im):
    new_image = Image.new("RGB",im.size,"black")
    pixels = new_image.load() #create the pixel map

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            rgb = im.getpixel((i,j))
            pixels[i,j] = (255 - rgb[0] , 255 - rgb[1], 255 - rgb[2])
    return new_image





im = Image.open("young-stalin.jpeg")
nw_im = negative(im)
nw_im.show()