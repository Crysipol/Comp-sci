#Name: Kevin Paute
#Date: October 2, 2023

s = input("Enter a String:")
ls = len(s)

for i in range(ls):
    print(s[:i])

for i in range(ls):
    print(s[i:])

print("Goodbye :)")