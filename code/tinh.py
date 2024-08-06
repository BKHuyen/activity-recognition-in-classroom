import matplotlib.pyplot as plt
import os
import math
#import matplotlib.patches as patches
from PIL import Image
file_path = 'raising_hand/data/grt.txt'
txtpath = 'raising_hand/raisinghand_label_image/labels/'
i=0
lns = []
merged_text = ""
def round_up(n, decimals = 0):
    multiplier = 10 ** decimals
    return math.ceil(n*multiplier) / multiplier

for intxtfile in os.listdir(txtpath):
    if intxtfile.endswith(".txt"):
        f = open(f'{txtpath}{intxtfile}')
        f = f.read()
        i += 1
        f = f.split("\n")
      
        for lns in f:
            if lns != '':
                lns = lns.split(" ")   
                id = lns[0]
                w = float(lns[3])*1920
                h = float(lns[4])*1080
                xc = float(lns[1])
                x1 = float(xc*1920-w/2)
                yc = float(lns[2])
                y1 = yc*1080 - h/2
                if(i == 167): 
                    i += 41
              
                merged_text += str(i) + " " + str(id) + " " + str(int(x1)) + " " + str(int(y1)) + " " + str(int(round_up(w))) + " " + str(int(round_up(h))) + "\n"
                print(i)
    

    with open(file_path, 'w') as file:
            file.write(merged_text) 
    
       

       
        