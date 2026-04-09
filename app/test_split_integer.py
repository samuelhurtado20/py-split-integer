from app.split_integer import split_integer


def test_sum_or_parts_should_be_equal_to_value():
    # Prueba que la suma de las partes coincida con el valor original
    result = split_integer(17, 4)
    assert sum(result) == 17


def test_split_integer_should_split_into_equal_parts():
    # Caso donde el valor es perfectamente divisible
    assert split_integer(6, 2) == [3, 3]


def test_parts_should_be_sorted_ascending():
    # Verifica que el array resultante esté ordenado
    result = split_integer(32, 6)
    assert result == sorted(result)


def test_difference_between_maximum_and_minimum_value_should_be_less_or_equal_to_one():
    # La parte más importante: la equidad en la distribución
    result = split_integer(32, 6)
    assert max(result) - min(result) <= 1


def test_should_return_part_equals_to_value_when_split_into_one_part():
    # Caso borde: dividir en una sola parte
    assert split_integer(8, 1) == [8]
