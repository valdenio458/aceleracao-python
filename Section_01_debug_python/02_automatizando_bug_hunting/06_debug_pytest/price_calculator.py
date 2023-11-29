def calculate_total_price(unit_price, quantity, discount):
    if (
        not isinstance(unit_price, (int, float))
        or not isinstance(quantity, (int))
        or not isinstance(discount, (int, float))
    ):
        raise TypeError("Invalid input types")

    if unit_price <= 0 or quantity <= 0 or discount < 0 or discount >= 100:
        raise ValueError("Invalid input values")

    subtotal = unit_price * quantity
    total = subtotal - subtotal * discount / 100
    # evidẽncia subtotal * (1 - discount / 100)

    return total
