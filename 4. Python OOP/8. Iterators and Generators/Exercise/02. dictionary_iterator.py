# class dictionary_iter:
#     def __init__(self, dict):
#         self.dict = dict
#         self.index = -1
#         self.list = [(x, y) for x, y in self.dict.items()]
#         self.len = len(self.list) - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.len > self.index:
#             self.index += 1
#             return self.list[self.index]
#         else:
#             raise StopIteration


class dictionary_iter:
    def __init__(self, dict):
        self.dict = dict
        self.index = -1
        self.list = [(x, y) for x, y in self.dict.items()]
        self.len = len(self.list) - 1

    def __iter__(self):
        return ((x, y) for x, y in self.dict.items())

    def __next__(self):
        if self.len == len(self.dict):
            raise StopIteration

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)


