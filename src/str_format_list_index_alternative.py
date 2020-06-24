list_value = [
    'タマ',
    5,
]
formatted_str = '飼っている猫の名前は{name}です。歳は{age}歳です。'
formatted_str = formatted_str.format(
    name=list_value[0],
    age=list_value[1],
)

print(formatted_str)