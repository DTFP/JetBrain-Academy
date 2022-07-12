msg_0 = 'Enter an equation'
msg_1 = 'Do you even know what numbers are? Stay focused!'
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = 'Yeah... division by zero. Smart move...'
msg_4 = 'Do you want to store the result? (y / n):'
msg_5 = 'Do you want to continue calculations? (y / n):'
msg_6 = ' ... lazy'
msg_7 = ' ... very lazy'
msg_8 = ' ... very, very lazy'
msg_9 = 'You are'
msg_10_12 = ['Are you sure? It is only one digit! (y / n)',
             "Don't be silly! It's just one number! Add to the memory? (y / n)",
             'Last chance! Do you really want to embarrass yourself? (y / n)']


def is_one_digit(v):
    if v.is_integer() and v > -10 and v < 10:
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


flag = True
memory = 0
while flag:
    print(msg_0)
    calc = input().split()
    x1 = calc[0]
    oper = calc[1]
    x2 = calc[2]
    if x1 == 'M':
        x1 = memory
    if x2 == 'M':
        x2 = memory
    try:
        x1 = float(x1)
        x2 = float(x2)
    except ValueError:
        print(msg_1)
        continue
    if oper not in ['+', '-', '*', '/']:
        print(msg_2)
        continue
    check(x1, x2, oper)
    if oper == '+':
        result = x1 + x2
        print(result)
    elif oper == '-':
        result = x1 - x2
        print(result)
    elif oper == '*':
        result = x1 * x2
        print(result)
    elif oper == '/' and x2 != 0:
        result = x1 / x2
        print(result)
    else:
        print(msg_3)
        continue
    while True:
        print(msg_4)
        store = input()
        if store != 'y' and store != 'n':
            continue
        elif store == 'y':
            if is_one_digit(result):
                msg_index = 10
                i = 0
                while msg_index <= 12:
                    print(f'{msg_10_12[i]}')
                    store = input()
                    if store != 'y' and store != 'n':
                        continue
                    elif store == 'y':
                        msg_index += 1
                        i += 1
                        continue
                    elif store == 'n':
                        break
            break
        elif store == 'n':
            break
    if store == 'y':
        memory = result
    while True:
        print(msg_5)
        future_calc = input()
        if future_calc != 'y' and future_calc != 'n':
            continue
        elif future_calc == 'y':
            break
        elif future_calc == 'n':
            flag = False
            break
