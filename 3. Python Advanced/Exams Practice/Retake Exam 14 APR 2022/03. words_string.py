def words_sorting(*word_list):
    word_dict = {}
    for word in word_list:
        ascii_value = sum(ord(x) for x in word)
        word_dict[word] = ascii_value

    if sum(word_dict.values()) % 2 != 0:
        word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    else:
        word_dict = sorted(word_dict.items(), key=lambda x: x[0])

    return_string = ''
    for pair in word_dict:
        return_string += str(pair[0]) + ' - ' + str(pair[1]) + '\n'

    return return_string


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))


