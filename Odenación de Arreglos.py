def ordenar_fila(matriz, fila):
    matriz[fila] = sorted(matriz[fila])
    return matriz

# Matriz de ejemplo (3x3)
matriz = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

fila_a_ordenar = 1
matriz_original = [fila.copy() for fila in matriz]  # Hacemos una copia de la matriz original

matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

print('Matriz original:')
for fila in matriz_original:
    print(fila)

print('\nMatriz con la fila ordenada:')
for fila in matriz_ordenada:
    print(fila)
