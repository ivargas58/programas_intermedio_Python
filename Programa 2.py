'''
Microempresa
Pequena empresa
Mediana empresa
Grande empresa
'''
def calcular_promedio(ingresos, años):
    return sum(ingresos) / años

def clasificar_empresa(promedio, trabajadores):
    if promedio <= 2000000 and trabajadores <= 10:
        return "Es una microempresa"
    elif promedio <= 10000000 and trabajadores <= 49:
        return "Su empresa es pequeña"
    elif promedio >= 50000000 and trabajadores <= 249:
        return "Su empresa es mediana"
    elif promedio >= 50000000 and trabajadores >= 250:
        return "Su empresa es grande"
    else:
        return "No se clasificó ninguna empresa"

def main():
    while True:
        x = int(input('Entre la cantidad de años a promediar. Si no deseas utilizar el programa, marque el 0: '))
        if x == 0:
            print('Gracias por usar nuestro programa.')
            break
        elif 1 <= x <= 6:
            ingresos = [float(input(f'Entre el ingreso bruto {i + 1}: ')) for i in range(x)]
            resultado = calcular_promedio(ingresos, x)
            
            trabajadores = int(input('Entre el número de trabajadores: '))
            clasificacion = clasificar_empresa(resultado, trabajadores)
            
            print(clasificacion)
        else:
            print('Entrada no válida. Intente de nuevo.')

if __name__ == "__main__":
    main()
