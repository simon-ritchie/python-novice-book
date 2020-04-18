int_variable = 100


def add_one():
    global int_variable
    int_variable += 1
    print(int_variable)


add_one()