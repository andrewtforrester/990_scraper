import pytesseract
from PIL import Image

im = Image.open('test.png')
img_string = pytesseract.image_to_string(im).split("\n")

# for s in img_string:
#     print(s)

# Function 

def ein_finder(s_array):
    switched = False
    for s in s_array:
        if switched:
            return s.split(" ")[-1]
        if not s.find("Employer identification number") == -1:
            switched = True

print("The org's EIN is " + ein_finder(img_string))
