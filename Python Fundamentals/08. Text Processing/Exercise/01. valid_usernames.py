usernames = input().split(", ")
valid_names = []
for name in usernames:
    if 3 <= len(name) <= 16:
        good_letters = True
        for letter in name:
            if not letter.isalpha() and not letter.isdigit() and not letter == "-" and not letter == "_" and not letter == " ":
                good_letters = False
                break
        if good_letters:
            valid_names.append(name)
print("\n".join(f"{name}" for name in valid_names))
