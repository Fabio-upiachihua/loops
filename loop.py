import logging

# Configuramos el nivel de logging
logging.basicConfig(level=logging.DEBUG)

# Inicializamos las listas vacías
array = []
empty_array = []

# Registramos el estado inicial de las listas
logging.debug(f'Initial array: {array}')
logging.debug(f'Initial empty_array: {empty_array}')

# Llenamos la lista `array` con números del 1 al 6
for i in range(1, 4):
    array.append(i)
    logging.debug(f'Array after adding {i}: {array}')  # Estado de `array` tras cada inserción

for i in range(4, 7):
    array.append(i)
    logging.debug(f'Array after adding {i}: {array}')  # Estado de `array` tras cada inserción

# Mostramos el contenido final de las listas
logging.info(f'Final array: {array}')  # Debería imprimir: [1, 2, 3, 4, 5, 6]
logging.info(f'Final empty_array: {empty_array}')  # Debería imprimir: []

# Función adicional para manipular listas
def manipulate_arrays(array, empty_array):
    # Crear una lista de cuadrados de los números en `array`
    squares = [x ** 2 for x in array]
    logging.debug(f'Squares of array elements: {squares}')

    # Filtrar números pares en `array`
    even_numbers = [x for x in array if x % 2 == 0]
    logging.debug(f'Even numbers in array: {even_numbers}')

    # Ordenar `array` en orden descendente
    sorted_array = sorted(array, reverse=True)
    logging.debug(f'Sorted array in descending order: {sorted_array}')

    return squares, even_numbers, sorted_array
