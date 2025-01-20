luku1=input("Anna leiviskä: ")
luku2=input("Anna naulat:")
luku3=input("Anna luodit: ")
leiviska_int =int(luku1)*20*32*0.0133
naula_int=int(luku2)*32*0.0133
luoti_float=int(luku3)*0.0133
kokonaispaino= float(leiviska_int+naula_int+luoti_float)
kokonaisluku =int(kokonaispaino)
desimaali=(kokonaispaino- kokonaisluku)*1000
print(f"Kiloa: {kokonaisluku}")
print(f"Grammat: {desimaali:.2f}")

