dict_value = {
    'name': 'タマ',
    'age': 5,
}
formatted_str = '飼っている猫の名前は{name}です。歳は{age}歳です。'
formatted_str = formatted_str.format_map(dict_value)
print(formatted_str)