import easygui_qt as easy
from easygui import *
import time
from black_white import *
from quantitization import *
from rotate_image_180 import *
from rotate_image_90 import *




def menu_choices():
    link_im = easy.get_file_names()
    old_im = Image.open(link_im[0])
    msgbox("Welcome to bizarre program!")
    msg ="What is your choice?"
    title = "Image Operations"
    choices = ["BW", "Rotate 180", "Rotate 90", "Quantum"]
    choice = choicebox(msg, title, choices)
    






def main():
    
    menu_choices()




main()