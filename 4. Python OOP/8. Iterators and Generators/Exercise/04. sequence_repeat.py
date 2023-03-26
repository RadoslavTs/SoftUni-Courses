class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = -1
        self.result = ''

    def __iter__(self):
        return self

    def __next__(self):
        while self.number > 0:
            if self.index + 1 >= len(self.sequence):
                self.index = 0
            else:
                self.index += 1
            self.number -= 1
            self.result = self.sequence[self.index]
            return self.result
        else:
            raise StopIteration


# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end ='')


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
