animal = '猫'
name = 'タマ'
age = 5
formatted_str = '飼っている{0}の名前は{2}です。歳は{1}歳です。'
formatted_str = formatted_str.format(animal, age, name)

print(formatted_str)