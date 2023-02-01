try:
    print(5)
    raise KeyError
except (KeyError, ValueError):
    print("Error")
