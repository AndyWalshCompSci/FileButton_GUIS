'''
Andy Walsh
File Button
Oct. 26
'''


from tkinter import *
import random
from PIL import Image
from tkinter import ttk
from tkinter import filedialog as fd

root=Tk()

#tkinter window
root.geometry("400x500")

#image grab
def select_files():
    global my_image
    filetypes = (('image files', '*.jpg .png'),('All files', '.*'))
    filename = fd.askopenfilename(title='Open files', initialdir='/', filetypes=filetypes)
    my_image = Image.open(filename)
    loop_img(my_image)

# add the parameter my_image to your function
def loop_img(my_image):
    rows = my_image.size[0]
    cols = my_image.size[1]
    red_slide = red_slider.get()
    green_slide = green_slider.get()
    blue_slide = blue_slider.get()

    skip_lines = spin.get()
    skip_lines_int = int(skip_lines)

    skip_pixels = spin_2.get()
    skip_pixels_int = int(skip_pixels)

# open button
open_button = ttk.Button(root,text='Open Files',command=select_files)
open_button.grid(row=0,column=4)

'''
def get_file():
    global my_image
    filename = input("please provide name of file:  ")
    my_image = Image.open(filename)
'''

def My_image():
    rows = my_image.size[0]
    cols = my_image.size[1]
    red_slide = red_slider.get()
    green_slide = green_slider.get()
    blue_slide = blue_slider.get()

    skip_lines = spin.get()
    skip_lines_int = int(skip_lines)

    skip_pixels = spin_2.get()
    skip_pixels_int = int(skip_pixels)

    rows = my_image.size[0]
    cols = my_image.size[1]
    print(rows, cols)

    px = my_image.load()
    for i in range(0, rows, skip_lines_int):

        start = random.randint(0, rows)
        end = random.randint(0, cols)
        nub = random.randint(1, 5)

        if i % 2 == 0:
            start = 0
        else:
            start = i

        for j in range(start, cols,skip_lines_int):
            red = random.randint(0,red_slide)
            green = random.randint(0,green_slide)
            blue = random.randint(0,blue_slide)

            '''
            red_str= red_slider.get()
            red = int(red_str)
            green_str = green_slider.get()
            green = int(green_str)
            blue_str = blue_slider.get()
            blue = int(blue_str)
            px[i, j] = (red, green, blue)
            '''
            px[i,j] = (red, green, blue)
    my_image.show()

#button
Glitch_it = Button(root, text='Glitch it', command=My_image)
Glitch_it.grid(row=0,column=2)

#rgb sliders
red_slider = Scale(root, from_=0, to_=255,orient=HORIZONTAL, background="red", fg="grey")
red_slider.grid(row=2, column=2)
green_slider = Scale(root, from_=0, to_=255, orient=HORIZONTAL, background="green", fg="grey")
green_slider.grid(row=2, column= 3)
blue_slider = Scale(root, from_=0, to_=255, orient=HORIZONTAL, background="blue", fg="grey")
blue_slider.grid(row= 2, column=4)


spin = Spinbox(root, from_=1, to=10)
spin.grid(row=0, column=3)
spin_2 = Spinbox(root, from_=1, to=10)
spin_2.grid(row=1, column=3)


root.mainloop()