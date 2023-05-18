def reversa(lista):
    lista.sort(reverse=True)
    return lista

pepe = [3, 123, 51, 1, 3, 4, 5, 6]

pepe.sort()
print(f"pepe: {pepe}")
print(f"pepe: {reversa(pepe)}")

# Orden de mayor a menor
# epep = reversa(pepe)
# print(f"pepe: {epep}")

def no_reversa(lista):
    lista.sort(reverse=False)
    return lista

def pepinson(nombre):
    print(nombre)

def ana(nombre):
    print(f"{nombre} hace otra cosa")