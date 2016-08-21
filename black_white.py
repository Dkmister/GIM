from PIL import Image

#===============================
#   Given a image, return a Image BW
#   
#===============================
def black_white(a_image):
    new_image = Image.new("L",a_image.size)
    xy = a_image.size
    w = xy[0]
    h = xy[1]
    
    for i in xrange(w):
        for j in xrange(h):
            rgb = im.getpixel((i,j))
            l = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
            
            

im = Image.open("young-stalin.jpeg")
black_white(im)

