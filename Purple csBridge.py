#Name: Kevin Paute
#Email: Kevin.paute88@myhunter.cuny.edu
#Date: September 18,2023
#This program loads an image, displays it, and then creates a new image

import matplotlib.pyplot as plt
import numpy as np

meow = input("Enter a PNG file:")
cat = input ("Enter new name:")
img = plt.imread(meow)                       

img2 = img.copy()        
img2[:,:,1] = 0           
img2[:,:,0] = 0

plt.imsave(cat, img2) 
