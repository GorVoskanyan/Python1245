def factorial(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result


def main():
    x = int(input('Enter x '))
    print(factorial(x))
    
if __name__ == '__main__':
    main()