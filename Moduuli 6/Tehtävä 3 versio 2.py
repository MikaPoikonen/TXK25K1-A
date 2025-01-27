def muunna(gallona):
    return print(f"{gallona * 3.785} litraa")
def main():
    while True:
        gallonat=int(input("Anna gallonat: "))

        if gallonat <0:
                break
                muunna(gallonat)
                main()