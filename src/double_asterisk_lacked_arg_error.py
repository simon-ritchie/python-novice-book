def add_three_value(x, y, z):
    total = x + y + z
    return total


argument_dict = {
    'x': 10,
    'z': 30,
}

add_three_value(**argument_dict)