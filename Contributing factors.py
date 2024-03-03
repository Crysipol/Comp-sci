#Name: Kevin Paute
#Email:Kevin.paute88@myhunter.cuny.edu
import pandas as pd

csvFile = input('Enter CSV file name: ')         
vlist = pd.read_csv(csvFile)   
print("Top three contributing factors for collisions:")
print(vlist["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3]) 
