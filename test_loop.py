import logging
import project

# Configuramos el nivel de logging
logging.basicConfig(level=logging.DEBUG)

# Prueba de bucles: llenamos la lista `array` con números del 1 al 6 y verificamos los resultados
def test_loop_testing():
    logging.debug("Starting loop tests")

    # Inicializamos las listas para el test
    array = []
    empty_array = []

    # Llenamos la lista `array` con números del 1 al 6
    for i in range(1, 4):
        array.append(i)
        logging.debug(f'Array after adding {i}: {array}')  # Estado de `array` tras cada inserción

    for i in range(4, 7):
        array.append(i)
        logging.debug(f'Array after adding {i}: {array}')  # Estado de `array` tras cada inserción

    # Ejecutamos la función principal para manipular listas
    squares, even_numbers, sorted_array = project.manipulate_arrays(array, empty_array)

    # Verificamos los resultados
    assert squares == [1, 4, 9, 16, 25, 36], f"Expected squares to be [1, 4, 9, 16, 25, 36], but got {squares}"
    assert even_numbers == [2, 4, 6], f"Expected even numbers to be [2, 4, 6], but got {even_numbers}"
    assert sorted_array == [6, 5, 4, 3, 2, 1], f"Expected sorted array to be [6, 5, 4, 3, 2, 1], but got {sorted_array}"

    logging.debug("Completed loop tests")

# Ejecutar las pruebas
if __name__ == "__main__":
    test_loop_testing()
    logging.info("All tests passed!")
