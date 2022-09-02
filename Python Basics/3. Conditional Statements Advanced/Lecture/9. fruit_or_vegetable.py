fruit = input()
fruit_type = str()
if fruit == "banana" or\
        fruit == "apple" or\
        fruit == "kiwi" or\
        fruit == "cherry" or\
        fruit == "lemon" or\
        fruit == "grapes":
    fruit_type = "fruit"
elif fruit == "tomato" or\
        fruit == "cucumber" or\
        fruit == "pepper" or\
        fruit == "carrot":
    fruit_type = "vegetable"
else:
    fruit_type = "unknown"
print(fruit_type)