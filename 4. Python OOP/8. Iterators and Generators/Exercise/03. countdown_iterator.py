class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        while self.count >= 0:
            result = self.count
            self.count -= 1
            return result
        else:
            raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")


# iterator = countdown_iterator(0)
# for item in iterator:
#     print(item, end=" ")
