from PIL import Image

#===============================
#   Given a image, return a Image Filtered
#   Using l = 0.299*r+0.587*g+0.114*b
#   Then aplying, returns a filtered image
#===============================
def filter_perfect_illusion(a_image):
    new_image = Image.new("RGB",a_image.size,"black")
    pixels = new_image.load()
    xy = a_image.size
    w = xy[0]
    h = xy[1]
    
    for i in xrange(w):
        for j in xrange(h):
            rgb = a_image.getpixel((i,j))
            l = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
            pixels[i,j] = (i,j,int(l))
    return new_image
            

im = Image.open("young-stalin.jpeg")
im.show()
nw_im = filter_perfect_illusion(im)
nw_im.show()

