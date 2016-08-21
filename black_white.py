from PIL import Image

#===============================
#   Given a image, return a Image BW
#   This is just a BS
#===============================
def black_white(a_image):
    new_image = Image.new("RGB",a_image.size,"black")
    pixels = new_image.load() #create the pixel map
    
    for i in range(a_image.size[0]):
        for j in range(a_image.size[1]):
            rgb = a_image.getpixel((i,j))
            l = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
            pixels[i,j] = (int(l),int(l),int(l))
    return new_image
    
            

im = Image.open("batman.jpeg")
nw_im = black_white(im)
nw_im.show()

