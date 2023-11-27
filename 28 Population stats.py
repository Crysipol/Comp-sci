#Name: Kevin Paute
#Email: kevin.paute88@myhunter.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd 

pop = pd.read_csv('nycHistPop.csv',skiprows=5)
A = input("Enter borough:")

print("Average population:", pop[A].mean())
print("Maximum population:", pop[A].max())
