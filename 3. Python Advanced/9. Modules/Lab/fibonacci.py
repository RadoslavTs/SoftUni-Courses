def fibonacci_creator(n):
    fibonacci_list = [0]
    for sequence in range(1, n+1):
        if sequence == 1:
            continue
        elif sequence == 2:
            fibonacci_list.append(1)
        else:
            fibonacci_list.append(fibonacci_list[sequence-3]+fibonacci_list[sequence-2])

    return fibonacci_list


def index_return(my_list, number):
    try:
        searched_index = my_list.index(number)
        return f'The number - {number} is at index {searched_index}'
    except ValueError:
        return f'The number {number} is not in the sequence'
