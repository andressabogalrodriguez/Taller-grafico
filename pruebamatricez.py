import random
Matriz = []
for _ in range(8):
    fila = []
    for _ in range(8):
        celda = [random.randint(0, 256) for _ in range(3)]
        fila.append(celda)
    Matriz.append(fila)
for fila in Matriz:
    print(fila)