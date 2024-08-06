import cv2
import numpy as np
import sys

#chuyển sang dạng xmin, xmax, ymin, ymax
data = []
with open ("using_phone/data/pre.txt", "r") as f:
    f = f.read()
    f = f.split("\n")
s = "frame"+ "\t" +"personID"+ "\t" +"xmin"+ "\t" +"xmax"+ "\t" +"ymin"+ "\t" +"ymax" + "\n"

for i in f:
    i = i.split("\t")
    data.append(i)

for boxes in data: 
    fr_id = int(boxes[0])      
    id = int(boxes[1])
    x1 = int(boxes[2])
    y1  = int(boxes[3])
    wbb= int(boxes[4])
    hbb = int(boxes[5])
    xmax = x1 + wbb
    ymax = y1 + hbb
    s += str(fr_id) + "\t" + str(id)+ "\t" + str(x1)+ "\t" + str(xmax)+ "\t" + str(y1)+ "\t" + str(ymax) + "\n"


with open ("using_phone/data/3.txt", "w") as f:
    f.write(s)
            


