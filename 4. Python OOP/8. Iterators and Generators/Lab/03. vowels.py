class vowels:
    def __init__(self, my_string):
        self.my_string = my_string
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.my_string):
            char = self.my_string[self.index]
            self.index += 1

            if char.lower() in self.vowels:
                return char
        if self.index >= len(self.my_string):
            raise StopIteration



my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
