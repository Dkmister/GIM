from PIL import Image

def list_intervals_shade(num_intervals):
    lst_i = []
    r = 255/num_intervals
    a1 = 255/r
    lst_i.append(a1)
    for i in xrange(2,num_intervals):
	lst_i.append(i * a1)
    return lst_i

def quantitization(a_image, shades):
    new_image = Image.new("RGB",a_image.size,"black")
    pixels = new_image.load()
    xy = a_image.size
    w = xy[0]
    h = xy[1]
    
    lst_i = list_intervals_shade(shades) 

    for x in xrange(w):
	for y in xrange(h):
	    rgb  = a_image.getpixel((i,j))
	    if (rgb[0] == rgb[1] and rgb[1] == rgb[2]):
		
