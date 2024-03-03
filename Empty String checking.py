#Name: Kevin Paute
#Email: Kevin.paute88@myhunter.cuny.edu

def frog():
    A = input("Enter a non-empty string:")
    if A == '':
        print("That was empty. Try again")
        frog()
    else:
        print("You entered:",A)

if __name__ == "__main__":
     frog()
