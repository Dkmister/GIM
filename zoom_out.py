def zoom_out2(a_image):
    xy = a_image.size
    w = xy[0]
    h = xy[1]
    new_image = Image.new("RGB",(2*w,2*h),"black")
    pixels_new = new_image.load()
    pixels_old = a_image.load()

    for i in xrange(2*w):
        for j in xrange(2*h):
            print i,j
    