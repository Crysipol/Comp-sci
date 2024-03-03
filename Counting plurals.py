A = input("Enter Nouns:")

Words = int(A.count(" "))
Plural = int(A.count("s "))

E = Plural/Words

print("Number of Words:", Words)
print("Fraction of your list that is plural is:", E)
