class Example:
    text = 'hiii'

    def print_text():
        coef = 4
        result = Example.text * coef
        return result


hi = Example

print(hi.print_text())

