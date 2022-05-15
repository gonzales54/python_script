# lambda
def main():
    # x = lambda a: a + 10
    # x = lambda a, b : a * b
    x = lambda a, b, c: a + b + c

    print(x(5, 6, 2))


def main1(n):
    return lambda a: a * n


hello = main1(2)

if __name__ == '__main__':
    print(hello(11))
