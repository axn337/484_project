#!/usr/bin/python
import os
from PIL import Image
import numpy as np

threshold=15
wd = os.getcwd()
print("Current directory is \""+wd+"\"")

files = os.listdir(wd)
images = list()

for name in files:
	debris = name.split('.')
	if (debris[-1] == 'png')&(not debris[0].startswith('filtered')):
		images.append(name)
		print("file name :"+name)

		#./pcl_pcd2png GolfBall1.pcd GolfBall1.png --scale auto --color mono --field z
		#newName=name.replace('.pcd','.png')
		im = Image.open(name)
		im = im.convert('RGBA')
		data = np.array(im)   # "data" is a height x width x 4 numpy array

		#red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
		#filtered = (red > threshold) & (blue >  threshold) & (green > threshold)
		#data[..., :-1][filtered.T] = (255, 255, 255) # Transpose back needed
		converted = np.where(data == 0, 0, 0)
		im2 = Image.fromarray(converted.astype('uint8'))
		
		#im2 = Image.fromarray(data)
		im2.save("filtered"+name)


