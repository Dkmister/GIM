import easygui_qt as easy
from easygui import *
from random import randint
from black_white import *
from quantitization import *
from rotate_image_180 import *
from rotate_image_90 import *
from filter_perfect_illusion import *




def menu_choices():
    link_im = easy.get_file_names()
    old_im = Image.open(link_im[0])
    msgbox("Welcome to bizarre program!")
    msg_ ="What is your choice?"
    title_ = "Image Operations"
    choices = ["BW", "Rotate 180", "Rotate 90", "Random Quantum","Filter PF"]
    choice = choicebox(msg_, title_, choices)
    
    old_im.show()

    if choice == "BW":
        nw_im = black_white(old_im)
        nw_im.show()
    if choice == "Rotate 180":
        nw_im = rotate_image_180(old_im)
        nw_im.show()
    if choice == "Rotate 90":
        nw_im = rotate_image_90(old_im)
        nw_im.show()
    if choice == "Filter PF":
        nw_im = filter_perfect_illusion(old_im)
        nw_im.show()
    if choice == "Random Quantum":
        nw_im = black_white(old_im)
        nw_im = quantitization(nw_im,randint(1,255))
        nw_im.show()

    namefile = filesavebox(msg="Salve a imagem", title="Save me", default=None)
    nw_im.save(namefile)
def main():
    menu_choices()

main()