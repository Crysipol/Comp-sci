#Name: Kevin Paute
#Email: Kevin.paute88@myhunter.cuny.edu

names = input("Enter names:")
E = names.split('; ')

for i in E:
    f = i.split(', ')
    print(f[1], f[0])



