
luku =int(input("Anna luku: "))
alkuluku=True #alkuluku on True kunnes false

for i in range(2, luku ): #käy luvut läpi numero kaksi syötettyyn lukuun 2-> luku
    if luku // i == luku / i:
        alkuluku = False #Jos on jaollinen jollain muulla menee false

if alkuluku:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")

