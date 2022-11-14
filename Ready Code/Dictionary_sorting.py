my_dictionary = {"b":100, "a": 97, "c": 50}
print(sorted(my_dictionary.items(), key = lambda key_value: (key_value[1], key_value[0])))
