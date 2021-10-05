if __name__ == '__main__':
    n= int(input("Ingrese la cantidad de numeros a ingresar:"))
    par= True
    for i in range(0,n):
        numero= int(input("Ingrese el numero"+" "+str(i+1)+":"))
        if(numero%2!=0):
            par= False


if par:
    print("Todos son pares")
else:
    print("No todos son pares")
