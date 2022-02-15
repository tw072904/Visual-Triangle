import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np




num1 = int(input("What is the first side length (Side A)? :"))
num2 = int(input("What is the second side length (Side B)? :"))

output = math.sqrt((num1 * num1) + (num2 * num2))

print("The length of side C of this right triangle is " + str(output) + ".")

plot = input("Type exit to exit the program, or press any other key to see your triangle visually. :")




num1ratio = num1/(output)

num1 = 100 * num1ratio

num2ratio = num2/output

num2 = 100 * num2ratio



xoffset = ((100 - num1)/2)
yoffset = ((100 - num2)/2)

if plot == "exit" or plot == "Exit":
    exit()
else:  




    line1 = plt.Line2D((xoffset, num1 + xoffset), (yoffset,yoffset), lw = 1.5)
    line2 = plt.Line2D((xoffset, xoffset), (yoffset, num2 + yoffset), lw=1.5)
    line3 = plt.Line2D((num1 + xoffset, xoffset), (yoffset, num2 + yoffset), lw=1.5)    
    
    fig, ax = plt.subplots()
    plt.gca().add_line(line1)
    plt.gca().add_line(line2)
    plt.gca().add_line(line3)

    angle = math.degrees(math.atan(num2/num1))
    #ax.text((xoffset + (num1 + xoffset))/2 , (yoffset + (num2 + yoffset))/2 , "test", rotation = angle)


    ax.set(xlim=(0, 100), ylim=(0, 100))
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    plt.axis('on')
    plt.show()