def add_one_to_dict_value(dict_value):
    dict_value['age'] += 1


cat_info_dict = {'age': 10}
add_one_to_dict_value(dict_value=cat_info_dict)
print(cat_info_dict)