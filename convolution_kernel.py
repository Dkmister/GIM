from PIL import Image
from black_white import *




def convolution_kernel_G(a_image):
    G = [[0.0625,0.125,0.0625],[0.125,0.25,0.125],[0.0625,0.125,0.0625]]
    new_image =Image.new("RGB",a_image.size,"black")
    pixels_new = new_image.load()
    xy = a_image.size
    w = xy[0]
    h = xy[1]

    for i in xrange(1,w-1):
        for j in xrange(1,h-1):
            rgb_a = a_image.getpixel((i-1,j-1))
            rgb_b = a_image.getpixel((i-1,j))
            rgb_c = a_image.getpixel((i-1,j+1))
            rgb_d = a_image.getpixel((i,j-1))
            rgb_e = a_image.getpixel((i,j))
            rgb_f = a_image.getpixel((i,j+1))
            rgb_g = a_image.getpixel((i+1,j-1))
            rgb_h = a_image.getpixel((i+1,j))
            rgb_i = a_image.getpixel((i+1,j+1))
            conv_e_r = float(rgb_a[0]) * G[0][0] + float(rgb_b[0])* G[0][1] + float(rgb_c[0]) * G[0][2] + float(rgb_d[0]) * G[1][0] + float(rgb_e[0]) * G[1][1] + float(rgb_f[0]) * G[1][2] + float(rgb_g[0]) * G[2][0] + float(rgb_h[0]) * G[2][1] + float(rgb_i[0]) *G[2][2]
            conv_e_r = int(conv_e_r)
            pixels_new[i,j] = (conv_e_r,conv_e_r,conv_e_r)
    return new_image

def convolution_kernel_L(a_image):
    G = [[0,-1,0],[-1,4,-1],[0,-1,0]]
    new_image =Image.new("RGB",a_image.size,"black")
    pixels_new = new_image.load()
    xy = a_image.size
    w = xy[0]
    h = xy[1]

    for i in xrange(1,w-1):
        for j in xrange(1,h-1):
            rgb_a = a_image.getpixel((i-1,j-1))
            rgb_b = a_image.getpixel((i-1,j))
            rgb_c = a_image.getpixel((i-1,j+1))
            rgb_d = a_image.getpixel((i,j-1))
            rgb_e = a_image.getpixel((i,j))
            rgb_f = a_image.getpixel((i,j+1))
            rgb_g = a_image.getpixel((i+1,j-1))
            rgb_h = a_image.getpixel((i+1,j))
            rgb_i = a_image.getpixel((i+1,j+1))
            conv_e_r = float(rgb_a[0]) * G[0][0] + float(rgb_b[0])* G[0][1] + float(rgb_c[0]) * G[0][2] + float(rgb_d[0]) * G[1][0] + float(rgb_e[0]) * G[1][1] + float(rgb_f[0]) * G[1][2] + float(rgb_g[0]) * G[2][0] + float(rgb_h[0]) * G[2][1] + float(rgb_i[0]) *G[2][2]
            conv_e_r = int(conv_e_r)
            pixels_new[i,j] = (conv_e_r,conv_e_r,conv_e_r)
    return new_image



# Tests:
# >> convolution_kernel_G working -> OK
im = Image.open("young-stalin.jpeg")
nw_im = black_white(im)
nw_im.show()
cvl_im = convolution_kernel_L(nw_im)
cvl_im.show()