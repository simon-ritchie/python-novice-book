list_value = [
    'タマ',
    5,
]
formatted_str = '飼っている猫の名前は{0[0]}です。歳は{0[1]}歳です。'
formatted_str = formatted_str.format(list_value)

print(formatted_str)