#Name: Kevin Paute
#Email: Kevin.paute88@myhunter.cuny.edu

import matplotlib.pyplot as plt
import numpy as np 

A = int(input("Enter a Size:"))
B = input("Enter output file:")
img = np.ones((A,A,3))
img[:,:,2] = 0
img[::2,:,1] = 0
img[::2,:,2] = 1

plt.imsave(B, img)
