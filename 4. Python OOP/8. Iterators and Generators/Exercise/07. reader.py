def read_next(item, *args):
    yield item
    for x in args:
        if isinstance(x, dict):
            for k, v in x.items():
                yield k
        else:
            for y in x:
                yield y


# for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
#     print(item, end='')


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)

