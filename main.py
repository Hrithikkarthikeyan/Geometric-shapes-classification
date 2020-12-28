import numpy as np
import cv2
import math
from collections import OrderedDict

Answer = []
img = cv2.imread('images/grid_2.jpg')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
count = 1


for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    M = cv2.moments(contour)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    x, y, w, h = cv2.boundingRect(approx)
    temp_x = math.ceil((x-35)/139)
    temp_y = math.ceil((y-27)/139)
    grid_number = temp_x+(temp_y-1)*5
    if len(approx) == 3:
        b, g, r = img[x + 50, y + 50]
        if (b > g and b > r):
            color = "Blue"
        elif (g > b and g > r):
            color = "Green"
        else:
            color = "red"
        cv2.putText(img, "Triangle "+str(grid_number)+ " "+ color+" "+ str(cX)+" "+str(cY), (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 50, 250))
        Answer.append(["Triangle", color,grid_number,cX,cY])
    elif len(approx) == 4:
        if((w == 135 or w==134) and h == 135):
            #cv2.putText(img, str(x)+" "+str(y)+" "+ str(26 - count), (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 50, 250))
            count+=1
        elif(w<130 and h<130 and w>30 and h>30):
            b, g, r = img[cX, cY]
            if (b > g and b > r):
                color = "Blue"
            elif (g > b and g > r):
                color = "Green"
            else:
                color = "red"
            print(cX,cY,b,g,r)
            cv2.putText(img, "Quadrilateral "+str(grid_number) +" "+color+" "+ str(cX)+" "+str(cY), (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 50, 250))
            Answer.append(["Quadrilateral", color, grid_number, cX, cY])
    elif len(approx) == 5:
        b, g, r = img[cX,cY]
        if (b > g and b > r):
            color = "Blue"
        elif (g > b and g > r):
            color = "Green"
        else:
            color = "red"
        print(cX, cY, b, g, r)
        cv2.putText(img, "Pentagon "+str(grid_number) +" "+color+" "+ str(cX)+" "+str(cY), (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 50, 250))
        Answer.append(["Pentagon", color, grid_number, cX, cY])
    elif len(approx) == 6:
        b, g, r = img[x + 50, y + 50]
        if (b > g and b > r):
            color = "Blue"
        elif(g > b and g > r):
            color = "Green"
        else:
            color = "red"
        #print(x + 50, y + 50, b, g, r)
        cv2.putText(img, "Hexagon "+str(grid_number) + " "+color+" "+ str(cX)+" "+str(cY), (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 50, 250))
        Answer.append(["Hexagon", color, grid_number, cX, cY])
    else:
        b, g, r = img[x + 50, y + 50]
        if (b > g and b > r):
            color = "Blue"
        elif (g > b and g > r):
            color = "Green"
        else:
            color = "red"
        cv2.putText(img, "Circle "+str(grid_number)+ " "+ color+" "+ str(cX)+" "+str(cY), (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 50, 250))
        Answer.append(["Circle", color, grid_number, cX, cY])

rev = Answer.reverse()
print(Answer)
cv2.imshow("shapes",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
