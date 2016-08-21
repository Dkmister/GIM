from PIL import Image

#===============================
#   Given a image, return a Image BW
#   Using L = 0.299 * red + 0.587 * green + 0.114 * blue
#   Where rgb[0] = red , rgb[1] = green , rgb[2] = blue
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
    
            
#-------------------------------------
#   Tests using a image 1920x1080 => FULL HD
#   Status = OK
#-------------------------------------
im = Image.open("batman.jpeg")
nw_im = black_white(im)
nw_im.show()

