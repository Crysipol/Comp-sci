#Name: Kevin Paute
#Email: kevin.paute88@myhunter.cuny.edu

import pandas as pd
import matplotlib.pyplot as plt

Data = input('Enter name of input file: ')
DataOut = input('Enter name of output file: ')
homeless = pd.read_csv(Data)

homeless['Fraction Children'] = homeless['Total Children in Shelter']/homeless['Total Individuals in Shelter']
homeless.plot(x = "Date of Census", y = "Fraction Children")

fig = plt.gcf()
plt.savefig(DataOut) 