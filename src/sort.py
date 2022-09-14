def reversa(lista):
    lista.sort(reverse=True)
    return lista


pepe = [3, 1, 2]

pepe.sort()
print(f"pepe: {pepe}")

# Orden de mayor a menor
epep = reversa(pepe)
print(f"pepe: {epep}")
