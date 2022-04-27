import tkinter as tk
import re

#                   < Program settings / directory >
# This const is not nessecary, however it will make it easier to change the rendered image

FILE = r"bingus.txt"
line_data = open(FILE, "r").readlines()

magnification = 4
is_borderless = False
window_title = FILE


#                   < Parsing file and relocatating data >
# Inorder to store bits in the 2D list "lines", we need to extract the bits from the requested line in "FILE"
# To get all the bits in a line we grab all the requested characters with a regular expressions pattern
# Once the all the characters have been grabbed we can set them to a "line" in "lines", this provides ease of acsess
# By creating a 2D list we can store each line as an index ie: line[1] --> y pos 2

pat = re.compile(r"0|1")
lines = [pat.findall(line) for line in line_data]


#                   < Finding image properties & sizes >
# Inorder to store any data inside the 2D list "lines" we need to have some background information
# We also require this information to create a tkinter window (height, width, magnification)
# To avoid the indexing of non existant data we need to check if there is any data,
# We can do this by checking if the list is False (empty), if not empty --> continue

if(bool(line_data[0]) != False):
    x_size = len(lines[0]) # Grab length of line
    y_size = len(lines) # Grab number of lines

else:
    raise RuntimeError(":: FILE MUST CONTAIN BINARY DATA ::")


#                   < Creating window & setting magnifaction >
# Once we have the prerequiste information to render the image, we can prepare a tkinter window to display the image
# Since the size arguments of the function "geometry" require a string rather than an int, so we must convert the args
# x_size & y_size to strings. If magnifaction is required --> multiply value by magnification value --> convert to string
# Note magnification is pseudo, in reality the size of the pixel is being changed, essiently this enlarges an image.

window = tk.Tk()
window.title(window_title)
window.geometry(str(x_size * magnification) + "x" + str(y_size * magnification))
window.overrideredirect(is_borderless) # if true --> set window to borderless


#                   < Creating canvas & defining pixels >
# Inorder to draw a pixel to the screen we need a way of display colours without directly utlizing graphical APIs like OpenGL
# We can utlize the tkinter Canvas function to render pixels without interacting with these low level APIs in c / c++
# Since the tkinter Canvas has no direct function to render a pixel we can utlize the create_rectangle function instead
# This provides us with benfits a pixel function can not, for example: magnify a pixel --> we can change the 2nd set of x & y cords

viewport = tk.Canvas(window, width=str(x_size * magnification), height=str(y_size * magnification), bg="black", highlightthickness=0)

def draw_pixel(x, y, bit):
    if(str(bit) == "1"):
        bit_colour = "white"
    else:
        bit_colour = "black"

    viewport.create_rectangle(x, y, x + magnification, y + magnification, outline=bit_colour, fill=bit_colour)

#                   < Rendering image & closing statments >
# To render each pixel to the canvas (viewport) we need to utlize for-loops to itterate through the y_size & x_size
# For every "line" in the "lines" we need to print each bit as a pixel, to do this we can call the draw_pixel function definded above

for y_count in range(y_size):
    for x_count in range(x_size):
        draw_pixel(x_count * magnification, y_count * magnification, lines[y_count][x_count])

viewport.pack()
window.mainloop()

# Kaitlyn Williams 2022
# Apache 2.0 License
# 📝 File reading & Logical Error Solving 📝