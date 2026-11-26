# Primer repetido
# Dada una lista de números, devolver el PRIMER número que aparece por segunda vez al recorrer la lista. Si ninguno se repite, devolver None.

def primer_repetido(nums):
    vistos = set()

    for numero in nums:
        if numero in vistos:
            return numero
        else:
            vistos.add(numero)
    return None


print(primer_repetido([3, 1, 4, 1, 5, 3]))   # debería dar 1
print(primer_repetido([2, 7, 9, 7, 2]))      # debería dar 7
print(primer_repetido([1, 2, 3]))            # debería dar None