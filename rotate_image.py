from PIL import Image

#===============================
#   Given a image, return a Image matrix with
#   Inverted values of the original one
#===============================
def rotate_image(a_image):
    zero_triples = (0,0,0)
    xy = a_image.size
    w = xy[0]
    h = xy[1]
    # new_image = zero_triples[w][h]
    for i in xrange(0,w-1):
        for j in xrange(0,h-1):
            rgb = im.getpixel((i,j))
            # new_image[w-i-1][h-j-1] += rgb[i][j]

im = Image.open("young-stalin.jpeg")
rotate_image(im)

