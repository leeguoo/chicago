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


df = df[df["Primary Type"].isin(["ROBBERY","ASSAULT","BATTERY"])]
df = df[df["Location Description"].isin(["STREET","SIDEWALK","ALLEY"])]

hours = [datetime.strptime(timestr,"%m/%d/%Y %I:%M:%S %p").hour for timestr in list(df.Date)]

df["hour"] = hours

for i in range(24):
	df1 = df[df.hour==i]
	
	plt.figure(figsize=(6, 5), dpi=80, facecolor='w', edgecolor='k')
	
	y = list(df1["Latitude"])
	x = list(df1["Longitude"])
	
	plt.hist2d(x, y, bins=100, vmax=35,range=np.array([(xmin, xmax), (ymin, ymax)]))
	
	#plt.title("Robbery, assualt, and battery\n on streets, sidewalks, and alleys")
	plt.text(-87.95,41.65,"Hour: "+str(i),color="white")
	plt.xlim([xmin,xmax])
	plt.ylim([ymin,ymax])
	plt.xlabel("Latitude")
	plt.ylabel("Longtitude")
	plt.xticks([])
	plt.yticks([])
	plt.colorbar()
	
	plt.axes().set_aspect('equal')
	
#	plt.show()
	plt.savefig(str(i)+".gif")

