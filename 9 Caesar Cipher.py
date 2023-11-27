#Name: Kevin Paute 
#Email: Kevin.paute88@myhunter.cuny.edu
#Date: September 5, 2023
#This program prints: phrases to coded messages

for c in range(65,90):
    print(chr(c))
dough = input("Enter a phrase:")
bread = ""
for i in dough:
    offset = ord(i) - ord("a") + 13
    wrap = offset % 26
    newChar = chr(ord("a") + wrap)
    print(wrap, chr(ord("a") + wrap))
    bread = bread + newChar
print("The coded message is:", bread)
