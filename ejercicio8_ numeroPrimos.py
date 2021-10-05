def comprobarNumeroPrimo(numero):
     multiplicacion=1
     for i in range(1,numero):
        multiplicacion=multiplicacion*i
        if i==numero-1:
            break
     resultado= (multiplicacion+1)%numero==0
     return resultado


if __name__ == '__main__':
    numero= int(input("Ingrese el numero que quiere comprobar:"))
    resultado= comprobarNumeroPrimo(numero)
    contador=0
    if numero !=1:
     if resultado:
      for i in range(2,numero):
          if comprobarNumeroPrimo(i):
              contador= contador+1
      print("La cantidad de numeros primos que hay entre 1 y "+str(numero)+" es: "+str(contador))
     else:
      print("Lo sentimos,no es primo")
    else:
        print("Lo sentimos no es primo")

