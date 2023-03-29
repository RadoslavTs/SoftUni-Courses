from time import sleep, time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'The execution time of {func.__name__}was {end - start} seconds')
        return result

    return wrapper


@measure_time
def my_func(n):
    sleep(n)


my_func(2)