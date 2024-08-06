import matplotlib.pyplot as plt
import os
#import matplotlib.patches as patches
from PIL import Image
imginpath = 'raising_hand/2023-09-07_label_image/images/'
imgoutpath = 'raising_hand/data/sai26/'
txtpath = 'raising_hand/labels_id/pre/27/'

for intxtfile in os.listdir(txtpath):
    if intxtfile.endswith(".txt"):
      imginfile = f'{imginpath}{intxtfile[:-4]}.jpg'
      imgoutfile = f'{imgoutpath}{intxtfile[:-4]}.jpg'
      print(imginfile, imgoutfile)
      f = open(f'{txtpath}{intxtfile}')
      plt.figure(figsize=(16,10))
      im = Image.open(imginfile)
      # im.show()
      plt.figure(figsize=(16,10))
      ax = plt.gca()
      ax.imshow(im)
      for lines in f:
        lns = lines.split()
        id = lns[0]
        w = float(lns[3])*1920
        h = float(lns[4])*1080
        xc = float(lns[1])
        x1 = xc*1920-w/2
        yc = float(lns[2])
        y1 = yc*1080 - h/2
        rect = plt.Rectangle((x1, y1), w, h, fill=False, color='yellow', linewidth=2)
        plt.text(x1+w,y1+h,f'rh\n{id}', fontsize = 12, color = 'yellow')
        ax.add_patch(rect)
      ax.set_axis_off()
      plt.savefig(imgoutfile, bbox_inches='tight')