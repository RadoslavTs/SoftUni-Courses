def type_check(type):

    def calculate(function):
        def wrapper(num):
            result = function(num)
            if isinstance(num, type):
                return result
            else:
                return 'Bad Type'
        return wrapper

    return calculate



@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

