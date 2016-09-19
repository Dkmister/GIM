from PIL import Image
########################
def zoom_in2(a_image):
    xy = a_image.size
    w = xy[0]
    h = xy[1]
    new_image = Image.new("RGB",(2*w,2*h),"black")
    pixels_new = new_image.load()
    pixels_old = a_image.load()

    for i in xrange(0,2*w):
        for j in xrange(0,2*h):
            if (i%2==0 and j%2==0):
                rgb = a_image.getpixel((i/2,j/2))
                pixels_new[i,j] = (rgb[0],rgb[1],rgb[2])
            elif(i%2!=0 and j%2==0):
                rgb_A = a_image.getpixel((i-1,j))
                rgb_B = a_image.getpixel((i+1,j))

                red = (rgb_A[0]+rgb_B[0])/2
                green = (rgb_A[1]+rgb_B[1])/2
                blue = (rgb_A[2]+rgb_B[2])/2

                pixels_new[i,j] = (red,green,blue)
            elif(i%2==0 and j%2!=0):
                rgb_A = a_image.getpixel((i,j-1))
                rgb_B = a_image.getpixel((i,j+1))

                red = (rgb_A[0]+rgb_B[0])/2
                green = (rgb_A[1]+rgb_B[1])/2
                blue = (rgb_A[2]+rgb_B[2])/2

                pixels_new[i,j] = (red,green,blue)
            else:
                rgb_A = a_image.getpixel((i-1,j))
                rgb_B = a_image.getpixel((i+1,j))
                rgb_C = a_image.getpixel((i,j-1))
                rgb_D = a_image.getpixel((i,j+1))

                red = (rgb_A[0]+rgb_B[0]+rgb_C[0]+rgb_D[0])/4
                green = (rgb_A[1]+rgb_B[1]+rgb_C[1]+rgb_D[1])/4
                blue = (rgb_A[2]+rgb_B[2]+rgb_C[2]+rgb_D[2])/4

                pixels_new[i,j] = (red,green,blue)

    return new_image
########################
im = Image.open("young-stalin.jpeg")
nw_i=zoom_in2(im)
nw_i.show()