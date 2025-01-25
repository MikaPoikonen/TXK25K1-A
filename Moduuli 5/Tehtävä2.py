lista=[]

while True:
    numero = input("Anna luku: ")
    if numero =="":
        break
    lista.append(int(numero))
lista.sort(reverse=True)

for i in lista[0:4]:
        print (i)