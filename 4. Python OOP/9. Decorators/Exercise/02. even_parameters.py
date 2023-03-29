def even_parameters(function):

    def wrapper(*args):
        all_even = True
        for el in args:
            if isinstance(el, int):
                if el % 2 != 0:
                    all_even = False
                    break
            else:
                all_even = False
        if all_even:
            return function(*args)
        else:
            return 'Please use only even numbers!'

    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
