x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())
x1_less_x2 = False
y1_less_y2 = False
inside = False
outside = False
border = False
if x1 < x2:
    x1_less_x2 = True
if y1 < y2:
    y1_less_y2 = True
if not x1_less_x2 and not y1_less_y2:
    if x > x1 and x < x2 and y > y1 and y < y2:
        inside = True
    elif x < x1 or x > x2 or y < y1 or y > y2:
        outside = True
    elif x == x1 and y >= y1 and y <= y2:
        border = True
    elif x == x2 and y >= y1 and y <= y2:
        border = True
    elif y == y1 and x >= x1 and x <= x2:
        border = True
    elif y == y2 and x >= x1 and x <= x2:
        border = True
if inside and not outside:
    print("Inside / Outside")
elif not inside and outside:
    print("Inside / Outside")
elif border:
    print("Border")