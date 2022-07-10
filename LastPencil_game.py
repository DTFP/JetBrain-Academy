import random


print("How many pencils would you like to use:")
n = input()
while not n.isnumeric() or int(n) <= 0:
    if not n.isnumeric() or int(n) < 0:
        print("The number of pencils should be numeric")
    if n.isnumeric() and int(n) == 0:
        print("The number of pencils should be positive")
    n = input()
n = int(n)
print("Who will be the first (user, bot)")
name = input()
while (name != 'user') and (name != 'bot'):
    print("Choose between 'user' and 'bot'")
    name = input()
print('|' * n)
while n > 0:
    if name == 'user':
        print(name, "'s", sep='', end=' ')
        print('turn!')
        x = input()
        while not x.isnumeric() or (int(x) < 1 or int(x) > 3 or int(x) > n):
            if not x.isnumeric() or (int(x) < 1 or int(x) > 3):
                print("Possible values: '1', '2' or '3'")
            if x.isnumeric() and int(x) > n:
                print("Too many pencils were taken")
            x = input()
        n -= int(x)
        if n != 0:
            print('|' * n)
        if n == 0:
            print("bot won!", end='')
            break
        name = 'bot'
    if name == 'bot':
        print(name, "'s", sep='', end=' ')
        print('turn!')
        if n % 4 == 0:
            x = 3
        elif n % 4 == 3:
            x = 2
        elif n % 4 == 2 or n == 1:
            x = 1
        else:
            x = random.randint(1, 3)
        n -= x
        print(x)
        if n != 0:
            print('|' * n)
        if n == 0:
            print("user won!", end='')
            break
        name = 'user'
