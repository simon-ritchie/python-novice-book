name_dict = {'cat_name': 'タマ'}
age_list = [5]

formatted_str = (
    '飼っている猫の名前は{name_dict[cat_name]}です。'
    '歳は{age_list[0]}歳です。'
).format(
    name_dict=name_dict,
    age_list=age_list,
)

print(formatted_str)