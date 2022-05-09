# 🍁 **mapleBinary** 🍁
mapleBinary is an open source psuedo binary image creator, writen in python 3.0 🐍. 
mapleBinary lets you display txt files with unicode binary characters as images in a tkinter window.


## How to use:
### 📝Storing images📝
All images are stored in txt files as a series of binary characters (0 / 1).
To create a custom image, follow the following steps:

    1. Create a new txt file in the same directory as main.py
    2. Go to https://www.dcode.fr/binary-image
    3. Upload your image to the site and enter your desired parameters (resolution over 150 can break)
    4. Copy the outputed string
    5. Paste the new string into your txt document

### 🎥 Displaying images 🎥
To display an image change the following values and follow these steps:

    1. Execute the program "main.py"
    2. Enter your desired magnification value (int) (values 1 through 20 work the best)
    3. Enter the name of the file you wish to display (ie: tower.txt)
    4. OPTIONAL --> Set the value of window_title to your desired title in an IDE (by defualt set to name of file chosen)
    5. OPTIONAL --> Set the variable "is_borderless" to your desired value in an IDE (True = borderless, False = bordered)

### ‼️ Current bugs ‼️
-     Large images throw index errors
