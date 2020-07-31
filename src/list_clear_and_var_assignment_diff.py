def clear_list(list_value):
    list_value.clear()


def assign_blank_list(list_value):
    list_value = []


list_value_1 = ['猫', '犬', '兎']
clear_list(list_value=list_value_1)
print('list_value_1:', list_value_1)

list_value_2 = ['猫', '犬', '兎']
assign_blank_list(list_value=list_value_2)
print('list_value_2:', list_value_2)
