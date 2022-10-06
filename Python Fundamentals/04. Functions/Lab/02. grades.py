grade = float(input())


def grades(number):
    if 2.99 >= number > 2.00:
        return "Fail"
    elif 3.00 >= number > 3.49:
        return "Poor"
    elif 4.49 >= number >= 3.50:
        return "Good"
    elif 5.49 >= number >= 4.50:
        return "Very Good"
    elif 6.00 >= number >= 5.50:
        return "Excellent"


print(grades(grade))
