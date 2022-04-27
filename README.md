#🍁 **mapleBinary** 🍁
mapleBinary is an open source binary image creator, written by Kaitlyn Williams (KateBin™) in python 3.0 🐍. 
mapleBinary lets you display txt files with binary characters within them as images in a tkinter window.


## How to use:
###📝Storing images📝
All images are stored in txt files as a series of binary characters (0 / 1).
To create a custom image, follow the following steps:
    1. Create a new txt file in the same directory as main.py
    2. Go to https://www.dcode.fr/binary-image
    3. Upload your image to the site and enter your desired parameters (resolution over 150 can break)
    4. Copy the outputed string
    5. Paste the new string into your txt document

###🎥 Displaying images 🎥
To display an image change the following values and follow these steps:
    1. Change the value of the constant FILE to the name of your txt file (as string incluiding .txt)
    2. Set the value of magnification to your desired value (int) (values 1 through 20 work the best)
    3. Change the value of is_borderless to your desired result (True = Borderless, False = Bordered)
    4. Set the value of window_title to your desired title (by defualt set to name of file chosen)
    5. Once all of the above variables have been set, compile & run the script to display the image

###Current bugs 
    1. Bits improperly displayed in certain images
    2. Large images throw index errors
    3. Images with large y dimensions display all black pixels rather than ther assigned pixels at the bottom of the image