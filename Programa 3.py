def calcular_tiempo(distancia, velocidad):
    return distancia / velocidad

def main():
    while True:
        x = int(input('Marque el 1 si desea utilizar el programa, sino marque el 0: '))
        if x == 1:
            distancia = float(input('Entre la distancia en millas que va a recorrer: '))
            velocidad = float(input('Entre la velocidad en millas por hora: '))
            tiempo = calcular_tiempo(distancia, velocidad)
            print(f'Recorrerá las millas indicadas en este tiempo: {tiempo:.2f} horas')
        elif x == 0:
            print('Gracias por usar mi programa.')
            break
        else:
            print('Entrada no válida. Intente de nuevo.')

if __name__ == "__main__":
    main()
