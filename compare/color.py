#!/usr/bin/python
import pandas as pd
import pylab as plt
import numpy as np
from datetime import datetime

df = pd.read_csv("Crimes_-_2001_to_present.csv")
#df = pd.read_csv("less.csv")
df = df.dropna()

xmin = -88.0
xmax = -87.5
ymin = 41.6
ymax = 42.1

df = df[df.Longitude>=xmin]
df = df[df.Longitude<=xmax]
df = df[df.Latitude>=ymin]
df = df[df.Latitude<=ymax]

plt.figure(figsize=(5, 9), dpi=80, facecolor='w', edgecolor='k')

#plt.axes().set_aspect('equal')

#subplot1
plt.subplot(211)

y = list(df["Latitude"])
x = list(df["Longitude"])

plt.hist2d(x, y, bins=100,range=np.array([(xmin, xmax), (ymin, ymax)]))

plt.title("All crime events")
plt.xlim([xmin,xmax])
plt.ylim([ymin,ymax])
plt.xlabel("Latitude")
plt.ylabel("Longtitude")
plt.xticks([])
plt.yticks([])
plt.colorbar()


#subplot2
plt.subplot(212)

df = df[df["Primary Type"].isin(["ROBBERY","ASSAULT","BATTERY"])]
df = df[df["Location Description"].isin(["STREET","SIDEWALK","ALLEY"])]

y = list(df["Latitude"])
x = list(df["Longitude"])

plt.hist2d(x, y, bins=100,range=np.array([(xmin, xmax), (ymin, ymax)]))

plt.title("Robbery, assualt, and battery\n on streets, sidewalks, and alleys")
plt.xlim([xmin,xmax])
plt.ylim([ymin,ymax])
plt.xlabel("Latitude")
plt.ylabel("Longtitude")
plt.xticks([])
plt.yticks([])
plt.colorbar()

plt.tight_layout(pad=0.4)#, w_pad=0.5, h_pad=1.0)

#plt.show()
plt.savefig("compare.pdf")

