laskuri = 0
while laskuri <5:
    tunnus =input("tunnus: ")
    salasana=input("salasana: ")
    if tunnus=="mika" and salasana=="kissa":
        print("tervetuloa")
        break
    laskuri +=1
if laskuri ==5:
    print("pääsy evätty")
