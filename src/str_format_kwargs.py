cat_name = 'タマ'
cat_age = 5
formatted_str = '飼っている猫の名前は{name}です。歳は{age}歳です。'
formatted_str = formatted_str.format(
    name=cat_name,
    age=cat_age,
)

print(formatted_str)