def naughty_or_nice_list(*kids, **cooling):

    not_found_list = []
    commands = []
    kid_dict = {
        'Nice': [],
        'Naughty': [],
        'Not found': []    }
    kids_list = kids[0]
    kid_names_only = []
    for name in kids_list:
        kid_names_only.append(name[1])
    kid_list_dict = {}
    kid_list_name_dict = {}

    for kid in kids_list:
        number = str(kid[0])
        name = kid[1]
        if number not in kid_list_dict.keys():
            kid_list_dict[number] = []
        kid_list_dict[number].append(name)
        if name not in kid_list_name_dict.keys():
            kid_list_name_dict[name] = []
        kid_list_name_dict[name].append(number)

    for comm in kids:
        if type(comm) == str:
            commands.append(comm)

    for command in commands:
        command = command.split('-')
        number = command[0]
        destination = command[1]
        if number in kid_list_dict.keys():
            if len(kid_list_dict[number]) == 1:
                kid_name = kid_list_dict[number][0]
                if destination == 'Nice':
                    kid_dict[destination].append(kid_name)
                elif destination == 'Naughty':
                    kid_dict[destination].append(kid_name)
                del kid_list_dict[number]
                for _ in range(len(kids_list)):
                    list_kid = kids_list[_][1]
                    list_num = str(kids_list[_][0])
                    if list_num == number and list_kid == kid_name:
                        del kids_list[_]
                        kid_names_only.remove(list_kid)
                        break

    for kid, destination in cooling.items():
        if kid in kid_list_name_dict.keys():
            if len(kid_list_name_dict[kid]) == 1 and kid in kid_names_only:
                kid_dict[destination].append(kid)
                number = kid_list_name_dict[kid][0]
                for _ in range(len(kids_list)):
                    list_kid = kids_list[_][1]
                    list_num = str(kids_list[_][0])
                    if list_num == number and list_kid == kid:
                        del kids_list[_]
                        break

    for kid in kids_list:
        kid_name = kid[1]
        # kid_dict["Not found"] = []
        kid_dict["Not found"].append(kid_name)

    return_string = ''
    nice_kids = ''
    naughty_kids = ''
    not_found_kids = ''
    if kid_dict['Nice']:
        nice_kids = f'{", ".join(kid_dict["Nice"])}'
    if kid_dict['Naughty']:
        naughty_kids = f'{", ".join(kid_dict["Naughty"])}'
    if kid_dict['Not found']:
        not_found_kids = f'{", ".join(kid_dict["Not found"])}'

    for place in kid_dict.keys():
        if place == "Nice" and nice_kids:
            return_string += f'{place}: {nice_kids}\n'
        if place == 'Naughty' and naughty_kids:
            return_string += f'{place}: {naughty_kids}\n'
        if place == 'Not found' and not_found_kids:
            return_string += f'{place}: {not_found_kids}'

    return return_string


print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
