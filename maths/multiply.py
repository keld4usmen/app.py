def multiply(*numbers):
    print(numbers)


multiply(2, 5, 6, 7, 9)

def multiply(*numbers):
    for number in numbers:
        print(number)


multiply(2, 5, 6, 7, 9)



def multiply(x, y):
    print( x * y)


multiply(2, 5)


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total        


print(multiply(2, 5, 6, 7, 9))