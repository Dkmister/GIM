from black_white import *
#================================
# Given a number of intervals of a Black and white Image
# Returns a list of the intervals
# Making a simple arithmetic progression
# An = A1 + r * (n-1)
# A0 = 0 
# R = 255/number_of_intervals
# list_intervals_shade(int) => list
#================================
def list_intervals_shade(num_intervals):
    lst_i = []
    a1 = float(255.00/float(num_intervals))
    lst_i.append(0)
    lst_i.append(a1)
    for i in xrange(2,num_intervals):
	    lst_i.append((i * a1))
    lst_i.append(255.0)
    return lst_i
#=======================================
# This function make a simple verification of the intervalar values of the list
# The special case of rgb = 0 is treated
# Because of the iteration when i=0, makes the image goes crazy
# Returns the medium value between intervals
# interval_verification(int,list) => int
#=======================================

def interval_verification(rgb,lst_intervals):
    if(rgb==0):
        return (lst_intervals[1])/2
    for i in xrange(len(lst_intervals)):
        if(float(rgb)<=lst_intervals[i] and i!=0):
            return ((lst_intervals[i-1] + lst_intervals[i])/2)
        
#========================================
# This function makes the process of quantitization,
# Using the other functions to valuate the conditions 
# Then returning the respective value of L
# Use the functions:
# list_intervals_shade(num_intervals)
# interval_verification(rgb,lst_intervals)
# Returns a Image, a class defined by PIL
# quantitization(Image, int) => Image
#========================================    
def quantitization(a_image, shades):
    new_image = Image.new("RGB",a_image.size,"black")
    pixels = new_image.load()
    xy = a_image.size
    w = xy[0]
    h = xy[1]
    
    lst_i = list_intervals_shade(shades) 

    for x in xrange(w):
        for y in xrange(h):
            rgb  = a_image.getpixel((x,y))
            if (rgb[0] == rgb[1] and rgb[1] == rgb[2]):
                l = interval_verification(rgb[0],lst_i)
                pixels[x,y] = (int(l),int(l),int(l))
    return new_image


