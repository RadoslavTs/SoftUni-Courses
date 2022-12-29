# def length_validation(username):
#     if 3 <= len(username) <= 16:
#         return True
#     return False
#
#
# def character_validation(username):
#     for character in username:
#         if not (character.isalnum() or character == "_" or character == "-"):
#             return False
#         return True
#
#
# def symbol_validation(username):
#     if " " in username:
#         return False
#     return True
#
#
# def username_validation(username):
#     if length_validation(username) and character_validation(username) and symbol_validation(username):
#         return True
#     return False
#
#
# usernames = input().split(", ")
# for name in usernames:
#     if username_validation(name):
#         print(name)


def length_is_valid(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def characters_are_valid(name):
    for character in name:
        if not (character.isalnum() or character == "_" or character == "-"):
            return False
    return True


def no_redundant_symbols_(name):
    if ' ' in name:
        return False
    return True


def username_validation(name):
    if length_is_valid(name) and characters_are_valid(name) and no_redundant_symbols_(name):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_validation(username):
        print(username)