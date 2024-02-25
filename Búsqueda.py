def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return True, (i, j)
    return False, None

# Matriz de ejemplo (3x3)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

valor_buscado = 5
encontrado, posicion = buscar_valor(matriz, valor_buscado)

if encontrado:
    print(f'El valor {valor_buscado} se encontró en la posición {posicion}')
else:
    print(f'El valor {valor_buscado} no se encontró en la matriz.')
