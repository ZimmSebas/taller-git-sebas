def reversa(lista):
    lista.sort(reverse=True)
    return lista

pepe = [3, 123, 51]

pepe.sort()
print(f"pepe: {pepe}")
print(f"pepe: {reversa(pepe)}")

# Orden de mayor a menor
# epep = reversa(pepe)
# print(f"pepe: {epep}")
