input_string = input()
vowels = ["a", "o", "u", "e", "i"]
result = [char for char in input_string if char.lower() not in vowels]
print("".join(result))