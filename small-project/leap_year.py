def main(num):
    if num % 4 == 0:
        if num % 100 == 0 and num % 400 != 0:
            print('Not leap year!')
        else:
            print('leap year!')


if __name__ == '__main__':
    # x = int(input('input here: '))
    main(2000)
