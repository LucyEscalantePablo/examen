def convertir(numero,base):
    if numero ==0:
        return '0'
    residuo = numero%base
    rta = convertir(numero//base,base)
    return rta + str(residuo)

n = int(input('Ingrese el número: '))
p = int(input('Ingrese la base: '))

print (f'El resultado es: {convertir (n,p)}')