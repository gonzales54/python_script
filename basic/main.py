def prac(x):
    if (x > 0):
        result = x + prac(x - 1)
        print(result)
    else:
        result = 0
    return result


prac(10)
