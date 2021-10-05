if __name__ == '__main__':
    numero=0
    totalGanancias=0
    while numero>=0:
        numero= int(input("Ingrese numero de toneladas:"))
        if numero>30:
            toneladas=numero*1000
            descuento=toneladas*0.3
            toneladas= toneladas-descuento
            totalGanancias=totalGanancias+toneladas
        elif numero>20 and numero<=30:
            toneladas=numero*1000
            descuento=toneladas*0.15
            toneladas= toneladas-descuento
            totalGanancias=totalGanancias+toneladas
        elif numero>=10 and numero<=20:
            toneladas=numero*1000
            descuento=toneladas*0.05
            toneladas= toneladas-descuento
            totalGanancias=totalGanancias+toneladas
        elif numero<0:
            print("Se realizo el calculo")
        else:
            toneladas= numero*1000
            totalGanancias=totalGanancias+toneladas

print("La Ganancia total es:"+" "+str(totalGanancias))
