# Contains Duplicate (LeetCode 217)
# Dada una lista de numeros, devolver True si algun numero se repite, False si todos son distintos.

def contains_duplicate(nums):
    vistos = set()

    for numero in nums:
        if numero in vistos:
            return True
        else:
            vistos.add(numero)
    return False


print(contains_duplicate([1, 2, 3, 1]))   # debería dar True
print(contains_duplicate([1, 2, 3, 4]))   # debería dar False