lukumin=0
lukumax=0
while True:
    luku = input("Anna luku")
    if luku == "":
        print("loppu")
        break
    else:
        if int(luku) < lukumin or lukumin == 0:
            lukumin = int(luku)

        if int(luku) > lukumax or lukumax == 0:
            lukumax =int(luku)
print (lukumin,lukumax)




