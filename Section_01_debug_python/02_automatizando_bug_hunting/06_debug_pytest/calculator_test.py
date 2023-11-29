import pytest

from price_calculator import calculate_total_price


# ----- Com parametrização -----
@pytest.mark.parametrize(
    "unit_price, quantity, discount, expected",
    [
        ("10", 10, 10, TypeError),
        (10, "10", 10, TypeError),
        (10, 10, "10", TypeError)
    ],
)
def test_type_error(unit_price, quantity, discount, expected):
    with pytest.raises(expected):
        calculate_total_price(unit_price, quantity, discount)


# ----- Sem parametrização -----
# def test_type_error_price():
#     with pytest.raises(TypeError):
#         calculate_total_price('10', 10, 10)


# def test_type_error_quantity():
#     with pytest.raises(TypeError):
#         calculate_total_price(10, '10', 10)


# def test_type_error_discount():
#     with pytest.raises(TypeError):
#         calculate_total_price(10, 10, '10')


@pytest.mark.parametrize(
    "unit_price, quantity, discount, expected",
    [
        (-2, 10, 10, ValueError),  # price
        (0, 10, 10, ValueError),  # price
        (10, -2, 10, ValueError),  # quantity
        (10, 0, 10, ValueError),  # quantity
        (10, 10, -5, ValueError),  # discount
        (10, 10, 100, ValueError),  # discount
        (10, 10, 105, ValueError),  # discount
    ],
)
def test_value_error(unit_price, quantity, discount, expected):
    with pytest.raises(expected):
        calculate_total_price(unit_price, quantity, discount)


@pytest.mark.parametrize(
    "unit_price, quantity, discount, expected",
    [
        (10, 2, 10, 18),  # price
        (20, 4, 10, 72),  # quantity
        (50, 2, 20, 80),  # discount
    ],
)
def test_correct_values(unit_price, quantity, discount, expected):
    assert calculate_total_price(unit_price, quantity, discount) == expected
