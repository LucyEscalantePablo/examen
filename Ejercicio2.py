#Implemente un programa para convertir un número decimal a hexadecimal
#ejm. el número 8642 en forma hexadecimal es: 21C2
listaHex = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
numeroDecimal = int(input('ingrese un número decimal: '))


def recursiva (numeroDecimal):
    auxili = []
    if cociente < 16:
        auxili.append(cociente)
        return cociente
    else:
        resto = numeroDecimal % recursiva(numeroDecimal,16)
        auxili.append(resto)
        cociente = numeroDecimal // recursiva(numeroDecimal)

        return resto, cociente


print(f'la conversión del numero decimal {numeroDecimal} a hexadecimal es {hexadecimal}')
