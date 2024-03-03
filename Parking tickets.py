#Name: Kevin Paute
#Email: Kevin.paute88@myhunter.cuny.edu
#Date: October 26, 2023

import pandas as pd

csvFile = input('Enter CSV file name: ')         #
tickets = pd.read_csv(csvFile)   
Attribute = input('Enter attribute:')
print("The 10 worst offenders are:")
print(tickets[Attribute].value_counts()[:10]) 
