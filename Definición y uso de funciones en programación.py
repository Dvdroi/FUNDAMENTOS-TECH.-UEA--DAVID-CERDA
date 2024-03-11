def calcular_temperatura_promedio(datos_temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad a lo largo de las semanas.

    Args:
    - datos_temperaturas (dict): Un diccionario que contiene datos de temperaturas de múltiples ciudades y semanas.
                                 El formato del diccionario debe ser: {ciudad: [temp_semana_1, temp_semana_2, ..., temp_semana_n]}

    Returns:
    - dict: Un diccionario que contiene la temperatura promedio de cada ciudad.
    """
    # Inicializar un diccionario para almacenar las temperaturas promedio
    temperatura_promedio_ciudad = {}

    # Iterar sobre cada ciudad y sus temperaturas semanales
    for ciudad, temperaturas_semana in datos_temperaturas.items():
        # Calcular la temperatura promedio para cada ciudad
        temperatura_promedio = sum(temperaturas_semana) / len(temperaturas_semana)

        # Almacenar la temperatura promedio en el diccionario
        temperatura_promedio_ciudad[ciudad] = temperatura_promedio

    # Devolver el diccionario con las temperaturas promedio de cada ciudad
    return temperatura_promedio_ciudad


# Ejemplo de datos diferentes
otros_datos_temperaturas = {
    'Ciudad_X': [18, 20, 22, 19],
    'Ciudad_Y': [15, 18, 21, 16],
    'Ciudad_Z': [25, 27, 30, 24]
}

# Llamada a la función con datos diferentes
resultados_otra_ciudad = calcular_temperatura_promedio(otros_datos_temperaturas)

# Imprimir resultados
for ciudad, temperatura_promedio in resultados_otra_ciudad.items():
    print(f"Temperatura promedio en {ciudad}: {temperatura_promedio}°C")
