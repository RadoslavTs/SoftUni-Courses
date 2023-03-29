def vowel_filter(function):

    def wrapper():
        vowel_letters = ['a', 'o', 'u', 'i', 'e']
        my_list = function()
        result = [x for x in my_list if x in vowel_letters]
        return result
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
