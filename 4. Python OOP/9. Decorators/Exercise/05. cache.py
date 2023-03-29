def cache(func):

    def wrapper(n):
        log = {}
        for i in range(n):
            log[i+1] = func(i)

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
