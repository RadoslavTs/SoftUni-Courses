input_string = input()
digits_string = ""
letters_string = ""
symbols_string = ""
for symbol in input_string:
    if symbol.isdigit():
        digits_string += symbol
    elif symbol.isalpha():
        letters_string += symbol
    else:
        symbols_string += symbol
print(digits_string)
print(letters_string)
print(symbols_string)
