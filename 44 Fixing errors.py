#Name: Kevin Paute
#Email: Kevin.paute88@myhunter.cuny.edu
#Modified by: Kevin :)

def convert(s):

    total = 0
     
    for c in s:
          total = total * 16
          ascii = ord(c)
          if ord('0') <= ascii <= ord('9'):
               #It's a decimal number, and return it as decimal:
               total = total+ascii - ord('0')
          elif ord("A") <= ascii <= ord('F'):
               #It's a hex number between 10 and 15, convert and return:
               total = total + ascii - ord('A') + 10
          elif ord('a') <= ascii <= ord('f'):
               #Check if they used lower case:
               #It's a hex number between 10 and 15, convert and return:
               total = total + ascii - ord('a') + 10
          else:   
            return(-1)
    return(total)

def main():
    hexString = input("Enter a number in hex: ")
    print("The number in decimal is", convert(hexString))


#Allow script to be run directly:
if __name__ == "__main__":
     main()