class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.len = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.len < 0:
            raise StopIteration
        else:
            index = self.len
            self.len -= 1
            return self.iterable[index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

print(reversed_list.iterable)