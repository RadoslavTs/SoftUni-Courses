def get_magic_triangle(num):
    result = []
    for _ in range(1, num+1):
        if _ == 1:
            result.append([1])
        elif _ == 2:
            result.append([1, 1])
        else:
            result.append([])
    for i in range(2, num):
        for k in range(i+1):
            if 0 <= k - 1 < len(result[k])-1:
                addition = result[i-1][k-1]+result[i-1][k]
                result[i].append(addition)
            else:
                result[i].append(result[i-1][k-1])

    return result


get_magic_triangle(5)