while True:#toistaa lausetta kunnes brake ehto täytyy. Jos ei brake niin loputon kysely.
    luku1=float (input("Anna tuumat: "))
    tuuma=luku1*2.54
    if luku1>=1:
        print (f"{tuuma} cm")
    elif luku1<=1:#elif määrittää ehdon brake
        break




