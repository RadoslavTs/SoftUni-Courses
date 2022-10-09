def grades(number):
    result = ""
    if 2.99 >= number >= 2.00:
        result = "Fail"
    elif 3.49 >= number >= 3.00:
        result = "Poor"
    elif 4.49 >= number >= 3.50:
        result = "Good"
    elif 5.49 >= number >= 4.50:
        result = "Very Good"
    elif 6.00 >= number >= 5.50:
        result = "Excellent"

    return result


grade = float(input())
print(grades(grade))
