name_key = 'name'
age_key = 'age'
dict_value = {
    name_key: 'タマ',
    age_key: 5,
}

formatted_str = '飼っている猫の名前は{name}です。歳は{age}歳です。'
formatted_str = formatted_str.format(
    name=dict_value[name_key],
    age=dict_value[age_key],
)

print(formatted_str)