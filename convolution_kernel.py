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
            conv_e_r = float(rgb_i[0]) * G[0][0] + float(rgb_h[0])* G[0][1] + float(rgb_g[0]) * G[0][2] + float(rgb_f[0]) * G[1][0] + float(rgb_e[0]) * G[1][1] + float(rgb_d[0]) * G[1][2] + float(rgb_c[0]) * G[2][0] + float(rgb_b[0]) * G[2][1] + float(rgb_a[0]) *G[2][2]
            conv_e_r = int(conv_e_r)
            conv_e_g = float(rgb_i[1]) * G[0][0] + float(rgb_h[1])* G[0][1] + float(rgb_g[1]) * G[0][2] + float(rgb_f[1]) * G[1][0] + float(rgb_e[1]) * G[1][1] + float(rgb_d[1]) * G[1][2] + float(rgb_c[1]) * G[2][0] + float(rgb_b[1]) * G[2][1] + float(rgb_a[1]) *G[2][2]
            conv_e_g = int(conv_e_g)
            conv_e_b = float(rgb_i[2]) * G[0][0] + float(rgb_h[2])* G[0][1] + float(rgb_g[2]) * G[0][2] + float(rgb_f[2]) * G[1][0] + float(rgb_e[2]) * G[1][1] + float(rgb_d[2]) * G[1][2] + float(rgb_c[2]) * G[2][0] + float(rgb_b[2]) * G[2][1] + float(rgb_a[2]) *G[2][2]
            conv_e_b = int(conv_e_b)
            if(conv_e_r>255):
                conv_e_r = 255
            elif(conv_e_r<0):
                conv_e_r = 0
            elif(conv_e_g>255):
                conv_e_g = 255
            elif(conv_e_g<0):
                conv_e_g = 0
            elif(conv_e_b>255):
                conv_e_b = 255
            elif(conv_e_b<0):
                conv_e_b = 0
            pixels_new[i,j] = (conv_e_r,conv_e_g,conv_e_b)
    return new_image


def convolution_kernel_PAG(a_image):
    G = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
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
            conv_e_r = float(rgb_i[0]) * G[0][0] + float(rgb_h[0])* G[0][1] + float(rgb_g[0]) * G[0][2] + float(rgb_f[0]) * G[1][0] + float(rgb_e[0]) * G[1][1] + float(rgb_d[0]) * G[1][2] + float(rgb_c[0]) * G[2][0] + float(rgb_b[0]) * G[2][1] + float(rgb_a[0]) *G[2][2]
            conv_e_r = int(conv_e_r)
            conv_e_g = float(rgb_i[1]) * G[0][0] + float(rgb_h[1])* G[0][1] + float(rgb_g[1]) * G[0][2] + float(rgb_f[1]) * G[1][0] + float(rgb_e[1]) * G[1][1] + float(rgb_d[1]) * G[1][2] + float(rgb_c[1]) * G[2][0] + float(rgb_b[1]) * G[2][1] + float(rgb_a[1]) *G[2][2]
            conv_e_g = int(conv_e_g)
            conv_e_b = float(rgb_i[2]) * G[0][0] + float(rgb_h[2])* G[0][1] + float(rgb_g[2]) * G[0][2] + float(rgb_f[2]) * G[1][0] + float(rgb_e[2]) * G[1][1] + float(rgb_d[2]) * G[1][2] + float(rgb_c[2]) * G[2][0] + float(rgb_b[2]) * G[2][1] + float(rgb_a[2]) *G[2][2]
            conv_e_b = int(conv_e_b)
            if(conv_e_r>255):
                conv_e_r = 255
            elif(conv_e_r<0):
                conv_e_r = 0
            elif(conv_e_g>255):
                conv_e_g = 255
            elif(conv_e_g<0):
                conv_e_g = 0
            elif(conv_e_b>255):
                conv_e_b = 255
            elif(conv_e_b<0):
                conv_e_b = 0
            pixels_new[i,j] = (conv_e_r,conv_e_g,conv_e_b)
    return new_image

def convolution_kernel_PHX(a_image):
    G = [[-1,0,1],[-1,0,1],[-1,0,1]]
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
            conv_e_r = float(rgb_i[0]) * G[0][0] + float(rgb_h[0])* G[0][1] + float(rgb_g[0]) * G[0][2] + float(rgb_f[0]) * G[1][0] + float(rgb_e[0]) * G[1][1] + float(rgb_d[0]) * G[1][2] + float(rgb_c[0]) * G[2][0] + float(rgb_b[0]) * G[2][1] + float(rgb_a[0]) *G[2][2]
            conv_e_r += 127
            conv_e_r = int(conv_e_r)
            conv_e_g = float(rgb_i[1]) * G[0][0] + float(rgb_h[1])* G[0][1] + float(rgb_g[1]) * G[0][2] + float(rgb_f[1]) * G[1][0] + float(rgb_e[1]) * G[1][1] + float(rgb_d[1]) * G[1][2] + float(rgb_c[1]) * G[2][0] + float(rgb_b[1]) * G[2][1] + float(rgb_a[1]) *G[2][2]
            conv_e_g += 127
            conv_e_g = int(conv_e_g)
            conv_e_b = float(rgb_i[2]) * G[0][0] + float(rgb_h[2])* G[0][1] + float(rgb_g[2]) * G[0][2] + float(rgb_f[2]) * G[1][0] + float(rgb_e[2]) * G[1][1] + float(rgb_d[2]) * G[1][2] + float(rgb_c[2]) * G[2][0] + float(rgb_b[2]) * G[2][1] + float(rgb_a[2]) *G[2][2]
            conv_e_b += 127
            conv_e_b = int(conv_e_b)
            if(conv_e_r>255):
                conv_e_r = 255
            elif(conv_e_r<0):
                conv_e_r = 0
            elif(conv_e_g>255):
                conv_e_g = 255
            elif(conv_e_g<0):
                conv_e_g = 0
            elif(conv_e_b>255):
                conv_e_b = 255
            elif(conv_e_b<0):
                conv_e_b = 0
            pixels_new[i,j] = (conv_e_r,conv_e_g,conv_e_b)
    return new_image

def convolution_kernel_PHYHX(a_image):
    G = [[-1,-1,-1],[0,0,0],[1,1,1]]
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
            conv_e_r = float(rgb_i[0]) * G[0][0] + float(rgb_h[0])* G[0][1] + float(rgb_g[0]) * G[0][2] + float(rgb_f[0]) * G[1][0] + float(rgb_e[0]) * G[1][1] + float(rgb_d[0]) * G[1][2] + float(rgb_c[0]) * G[2][0] + float(rgb_b[0]) * G[2][1] + float(rgb_a[0]) *G[2][2]
            conv_e_r += 127
            conv_e_r = int(conv_e_r)
            conv_e_g = float(rgb_i[1]) * G[0][0] + float(rgb_h[1])* G[0][1] + float(rgb_g[1]) * G[0][2] + float(rgb_f[1]) * G[1][0] + float(rgb_e[1]) * G[1][1] + float(rgb_d[1]) * G[1][2] + float(rgb_c[1]) * G[2][0] + float(rgb_b[1]) * G[2][1] + float(rgb_a[1]) *G[2][2]
            conv_e_g += 127
            conv_e_g = int(conv_e_g)
            conv_e_b = float(rgb_i[2]) * G[0][0] + float(rgb_h[2])* G[0][1] + float(rgb_g[2]) * G[0][2] + float(rgb_f[2]) * G[1][0] + float(rgb_e[2]) * G[1][1] + float(rgb_d[2]) * G[1][2] + float(rgb_c[2]) * G[2][0] + float(rgb_b[2]) * G[2][1] + float(rgb_a[2]) *G[2][2]
            conv_e_b += 127
            conv_e_b = int(conv_e_b)
            if(conv_e_r>255):
                conv_e_r = 255
            elif(conv_e_r<0):
                conv_e_r = 0
            elif(conv_e_g>255):
                conv_e_g = 255
            elif(conv_e_g<0):
                conv_e_g = 0
            elif(conv_e_b>255):
                conv_e_b = 255
            elif(conv_e_b<0):
                conv_e_b = 0
            pixels_new[i,j] = (conv_e_r,conv_e_g,conv_e_b)
    return new_image

def convolution_kernel_SHX(a_image):
    G = [[-1,0,1],[-2,0,2],[-1,0,1]]
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
            conv_e_r = float(rgb_i[0]) * G[0][0] + float(rgb_h[0])* G[0][1] + float(rgb_g[0]) * G[0][2] + float(rgb_f[0]) * G[1][0] + float(rgb_e[0]) * G[1][1] + float(rgb_d[0]) * G[1][2] + float(rgb_c[0]) * G[2][0] + float(rgb_b[0]) * G[2][1] + float(rgb_a[0]) *G[2][2]
            conv_e_r += 127
            conv_e_r = int(conv_e_r)
            conv_e_g = float(rgb_i[1]) * G[0][0] + float(rgb_h[1])* G[0][1] + float(rgb_g[1]) * G[0][2] + float(rgb_f[1]) * G[1][0] + float(rgb_e[1]) * G[1][1] + float(rgb_d[1]) * G[1][2] + float(rgb_c[1]) * G[2][0] + float(rgb_b[1]) * G[2][1] + float(rgb_a[1]) *G[2][2]
            conv_e_g += 127
            conv_e_g = int(conv_e_g)
            conv_e_b = float(rgb_i[2]) * G[0][0] + float(rgb_h[2])* G[0][1] + float(rgb_g[2]) * G[0][2] + float(rgb_f[2]) * G[1][0] + float(rgb_e[2]) * G[1][1] + float(rgb_d[2]) * G[1][2] + float(rgb_c[2]) * G[2][0] + float(rgb_b[2]) * G[2][1] + float(rgb_a[2]) *G[2][2]
            conv_e_b += 127
            conv_e_b = int(conv_e_b)
            if(conv_e_r>255):
                conv_e_r = 255
            elif(conv_e_r<0):
                conv_e_r = 0
            elif(conv_e_g>255):
                conv_e_g = 255
            elif(conv_e_g<0):
                conv_e_g = 0
            elif(conv_e_b>255):
                conv_e_b = 255
            elif(conv_e_b<0):
                conv_e_b = 0
            pixels_new[i,j] = (conv_e_r,conv_e_g,conv_e_b)
    return new_image

def convolution_kernel_SHY(a_image):
    G = [[-1,-2,-1],[0,0,0],[1,2,1]]
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
            conv_e_r = float(rgb_i[0]) * G[0][0] + float(rgb_h[0])* G[0][1] + float(rgb_g[0]) * G[0][2] + float(rgb_f[0]) * G[1][0] + float(rgb_e[0]) * G[1][1] + float(rgb_d[0]) * G[1][2] + float(rgb_c[0]) * G[2][0] + float(rgb_b[0]) * G[2][1] + float(rgb_a[0]) *G[2][2]
            conv_e_r += 127
            conv_e_r = int(conv_e_r)
            conv_e_g = float(rgb_i[1]) * G[0][0] + float(rgb_h[1])* G[0][1] + float(rgb_g[1]) * G[0][2] + float(rgb_f[1]) * G[1][0] + float(rgb_e[1]) * G[1][1] + float(rgb_d[1]) * G[1][2] + float(rgb_c[1]) * G[2][0] + float(rgb_b[1]) * G[2][1] + float(rgb_a[1]) *G[2][2]
            conv_e_g += 127
            conv_e_g = int(conv_e_g)
            conv_e_b = float(rgb_i[2]) * G[0][0] + float(rgb_h[2])* G[0][1] + float(rgb_g[2]) * G[0][2] + float(rgb_f[2]) * G[1][0] + float(rgb_e[2]) * G[1][1] + float(rgb_d[2]) * G[1][2] + float(rgb_c[2]) * G[2][0] + float(rgb_b[2]) * G[2][1] + float(rgb_a[2]) *G[2][2]
            conv_e_b += 127
            conv_e_b = int(conv_e_b)
            if(conv_e_r>255):
                conv_e_r = 255
            elif(conv_e_r<0):
                conv_e_r = 0
            elif(conv_e_g>255):
                conv_e_g = 255
            elif(conv_e_g<0):
                conv_e_g = 0
            elif(conv_e_b>255):
                conv_e_b = 255
            elif(conv_e_b<0):
                conv_e_b = 0
            pixels_new[i,j] = (conv_e_r,conv_e_g,conv_e_b)
    return new_image

# Tests:
# >> convolution_kernel_G working -> OK
# >> convolution_kernel_L working -> OK
# >> convolution_kernel_PAG working ->OK
# >> convolution_kernel_PHX working -> OK
# >> convolution_kernel_PHYHX working -> OK
im = Image.open("mi.jpg")
nw_im = black_white(im)
nw_im.show()
cvl_im = convolution_kernel_G(nw_im)
cvl_im.show()