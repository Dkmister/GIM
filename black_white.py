from PIL import Image

#===============================
#   Given a image, return a Image BW
#   This is just a BS
#===============================
def black_white(a_image):
    new_image = Image.new("L",a_image.size)
    xy = a_image.size
    w = xy[0]
    h = xy[1]
    
    for i in xrange(w):
        for j in xrange(h):
            rgb = a_image.getpixel((i,j))
            l = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
            print l
            rgb_new = new_image.getpixel((i,j))
            # rgb_new[0] = l
            # rgb_new[1] = l
            # rgb_new[2] = l
            # WHY THE FUCK CAN'T I DO THAT ?
            # WHAT'S SO FUCKING WRONG IN PROGRAMMING?
            # FUCK THIS SHIT!!!!
    return new_image
            

im = Image.open("young-stalin.jpeg")
nw_im = black_white(im)
nw_im.show()

