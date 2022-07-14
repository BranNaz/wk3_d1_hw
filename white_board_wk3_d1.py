def num(x):
    if x % 2 == 0:
        return 'FIZZ'
    elif x % 2 == 1:
        return 'BUZZ'

print(num(6))


def num(x):
    if x % 3 == 0 and x % 5 == 0:
        return 'FIZZBUZZ'
    elif x % 5 == 1:
        return 'BUZZ'
    elif x % 3 == 0:
        return 'FIZZ'
    else:
        return x
   

print(num(21))