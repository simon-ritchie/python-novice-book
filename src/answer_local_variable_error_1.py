dog_age = 10


def increment_dog_age():
    global dog_age
    dog_age += 1


increment_dog_age()
print(dog_age)