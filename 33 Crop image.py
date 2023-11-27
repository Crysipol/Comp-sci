#Name: Kevin Paute
#Email: Kevin.paute88@myhunter.cuny.edu
import matplotlib.pyplot as plt
import numpy as np

A = input("Enter a image name:")
B = input("Enter output file:")
img = plt.imread(A)
height = img.shape[0]
width = img.shape[1]

img2 = img[height//2:, :width//2]

plt.imsave(B, img2)
