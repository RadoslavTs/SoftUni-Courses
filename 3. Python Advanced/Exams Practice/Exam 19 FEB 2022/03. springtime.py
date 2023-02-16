def start_spring(**garden):
    my_dict = {}
    for key, value in garden.items():
        if value not in my_dict.keys():
            my_dict[value] = []
            my_dict[value].append(key)
        else:
            my_dict[value].append(key)
    return_string = ''
    for key, value in sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        return_string += key + ':\n'
        value = sorted(value)
        for item in value:
            return_string += f'-{item}\n'

    return return_string


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
