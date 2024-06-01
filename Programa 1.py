def calcular_impuestos(ingreso_bruto, impuesto_tipo):
    tasas = {
        1: 0.133,
        2: 0.236,
        3: 0.299
    }
    
    tax = ingreso_bruto * tasas[impuesto_tipo]
    taxventas = ingreso_bruto * 0.115
    taxmunicipal = ingreso_bruto * 0.005
    neto = ingreso_bruto - tax - taxventas - taxmunicipal
    
    return neto, tax, taxventas, taxmunicipal

def imprimir_resultados(neto, ingreso_bruto, tax, taxventas, taxmunicipal, tipo):
    tipos = {
        1: "individual",
        2: "asociación",
        3: "corporación"
    }
    
    print(f'Su valor neto de la empresa tipo {tipos[tipo]} es: {neto:.2f}')
    print(f'Su valor bruto es de: {ingreso_bruto:.2f}')
    print(f'Su impuesto son: {tax:.2f}')
    print(f'Su impuesto de ventas son: {taxventas:.2f}')
    print(f'Su impuesto municipal son: {taxmunicipal:.2f}')

def main():
    while True:
        x = int(input('Entre el valor 1 si desea calcular empresa individual, 2 para empresa asociación, y 3 para empresa corporación: '))
        if x in [1, 2, 3]:
            ingreso_bruto = float(input('Entre el ingreso bruto de la empresa: '))
            neto, tax, taxventas, taxmunicipal = calcular_impuestos(ingreso_bruto, x)
            imprimir_resultados(neto, ingreso_bruto, tax, taxventas, taxmunicipal, x)
        else:
            print('No entró ningún valor deseado, gracias por usar nuestro programa.')
            break

if __name__ == "__main__":
    main()
