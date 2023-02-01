def age_assignment(*args, **kwargs):
    result = []
    for name in sorted(args):
        for key, value in kwargs.items():
            if name.startswith(key):
                result.append((name, value))
    result_print = ''
    for name, age in result:
        result_print += f"{name} is {age} years old.\n"

    return result_print


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))