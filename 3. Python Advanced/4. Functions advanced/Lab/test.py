def calculator(operator):
    def addition(a, b):
        return a+b

    def subtraction(a, b):
        return a-b

    def division(a, b):
        return a/b

    def multiplication(a,b):
        return a*b

    if operator == "+":
        return addition

    elif operator == "-":
        return subtraction

    elif operator == "*":
        return multiplication

    elif operator == "/":
        return division


function_result = calculator("/")
print(function_result(1, 2))
