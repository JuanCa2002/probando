if __name__ == '__main__':
    numero= int(input("Ingrese el numero para saber si es perfecto:"))
    sumatoria=0
    for i in range(1,numero):
        if numero%i==0:
            sumatoria= sumatoria+i

if sumatoria==numero:
    print("!es perfecto¡")
else:
    print("!buuu, no es perfecto¡")
