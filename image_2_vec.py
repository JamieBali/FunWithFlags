import numpy as np
import os

from PIL import Image

import csv



# white
# black
# red
# yellow
# blue
# green
# orange

f = open("file.txt", "a")


imgName = ["newflag.png"]

for img in imgName:

    myImage = Image.open("C:/Users/PPGja/Pictures/flags/"+img)

    imgarray = np.array(myImage.convert("RGB"))

    output = []
    for x in imgarray:
        row = []
        for y in x:
            pixel = [0,0,0,0,0,0,0]
            #white
            if (y[0] == 255 and y[1] == 255 and y[2] == 255):
                pixel[0] = 1
            #black
            elif (y[0] == 0 and y[1] == 0 and y[2] == 0):
                pixel[1] = 1
            #red
            elif (y[0] == 255 and y[1] == 0 and y[2] == 0):
                pixel[2] = 1
            #yellow
            elif (y[0] == 255 and y[1] == 216 and y[2] == 0):
                pixel[3] = 1
            #blue
            elif (y[0] == 0 and y[1] == 38 and y[2] == 255):
                pixel[4] = 1
            elif (y[0] == 0 and y[1] == 148 and y[2] == 255):
                pixel[4] = 1
            #green
            elif (y[0] == 0 and y[1] == 127 and y[2] == 70):
                pixel[5] = 1
            elif (y[0] == 38 and y[1] == 127 and y[2] == 0):
                pixel[5] = 1
            elif (y[0] == 0 and y[1] == 127 and y[2] == 14):
                pixel[5] = 1            
            #orange
            elif (y[0] == 255 and y[1] == 106 and y[2] == 0):
                pixel[6] = 1
            else:
                print("sorry, don't recognise")
                print(img)
                print(y)
                exit(1)
            row.append(pixel)
        output.append(row)
    s = img.removesuffix(".png")
    tag = ''.join([i for i in s if not i.isdigit()])
    print([tag,np.array(output).flatten()])

f.close()
