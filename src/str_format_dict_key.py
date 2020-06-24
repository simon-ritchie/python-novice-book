dict_value = {
    'name': 'タマ',
    'age': 5,
}
formatted_str = \
    '飼っている猫の名前は{0[name]}です。歳は{0[age]}歳です。'
formatted_str = formatted_str.format(dict_value)

print(formatted_str)