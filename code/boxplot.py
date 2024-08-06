import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("standing/data/ss.csv")
df.head()



malignant = df[df['Classname']=='Raising_hand']['Frames']
benign = df[df['Classname']=='Standing_up']['Frames']
sleeping = df[df['Classname']=='Sleeping']['Frames']
usingphone = df[df['Classname']=='Using_phone']['Frames']
fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot([malignant,benign,sleeping,usingphone], labels=['Raising_hand', 'Standing_up','Sleeping','Using_phone'])

fig.savefig("slide/plotbox.png", dpi=72)
