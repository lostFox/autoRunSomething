#import PIL

#print('hello, world!')
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

# spam(0)
def collatz(num):
    if(num == 1):
        return True
    elif (num % 2 == 0):
        num /= 2
    else:
        num = num*3+1
    return collatz(num)

# print(collatz(3))
for i in range(1, 10000):
    if(collatz(i) == True):
        print(i, collatz(i))
