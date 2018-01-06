#!/usr/bin/env python3
'''
Zhiang Chen/Joseph Broderick
July,2016
'''
"Save the list of names in directory, and converts them into png files. "

import os
import subprocess

wd = os.getcwd()
print("Current directory is \""+wd+"\"")


name="pose_learning_1_2_2_12.pcd"
newName="pose_learning_1_2_2_12.png"
scale=0.5

subprocess.call('pcl_pcd2png '+name+' '+newName+' --field z --scale auto',shell=True)

