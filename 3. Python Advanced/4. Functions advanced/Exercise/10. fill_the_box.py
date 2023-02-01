def fill_the_box(*args):
    box_capacity = args[0] * args[1] * args[2]
    finish_index = args.index("Finish")
    cubes_to_fit = sum(args[3:finish_index])
    if cubes_to_fit < box_capacity:
        return f"There is free space in the box. You could put {box_capacity-cubes_to_fit} more cubes."
    else:
        return f"No more free space! You have {cubes_to_fit-box_capacity} more cubes."


# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))