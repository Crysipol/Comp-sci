#Name: Kevin Paute
#Email: Kevin.paute88@myhunter.cuny.edu

time = float(input("Enter hour (in 24 hour time)"))

if time < 12:
    print("Good Morning")

elif time < 17:
    print("Good Afternoon")

else:
    print("Good Evening")