#Name: Kevin Paute
#Email: kevin.paute88@myhunter.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5)
A = input("Enter borough name:")
B = input("Enter output file name:")

pop['Fraction'] = pop[A]/pop['Total']
pop.plot(x = 'Year', y = 'Fraction')

fig = plt.gcf()
fig.savefig(B)
