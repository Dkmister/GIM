import easygui_qt as easy 
from black_white import *
from quantitization import *
from rotate_image_180 import *
from rotate_image_90 import *

def init_image():
    link_im = easy.get_file_names()
    return link_im[0] 


def menu_choices(link_im):
    choices = ["Blank and White","Quantum of Solace","Spin Me Round 180","Like a record 90,baby!"]
    old_im = Image.open(link_im)
    old_im.show()
    #here reply = easy.get_choice("Choose an option:",choices=choices)
    






def main():
    link_im = init_image()
    menu_choices(link_im)




main()