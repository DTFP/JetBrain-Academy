import random


class Calculator:

    def __init__(self):
        self.result = None
        self.x1 = random.randint(2, 9)
        self.operator = random.choice(['+', '-', '*'])
        self.x2 = random.randint(2, 9)
        print(f'{self.x1} {self.operator} {self.x2}')

    def add(self, a, b):
        return a + b

    def mul(self, a, b):
        return a * b

    def sub(self, a, b):
        return a - b

    def calculate(self):
        if self.operator == '+':
            self.result = self.add(self.x1, self.x2)
        elif self.operator == '*':
            self.result = self.mul(self.x1, self.x2)
        elif self.operator == '-':
            self.result = self.sub(self.x1, self.x2)

    def answer(self, right_answers):
        while True:
            answer = input()
            try:
                answer = float(answer)
                if answer == self.result:
                    print('Right!')
                    right_answers += 1
                    break
                else:
                    print('Wrong!')
                    break
            except ValueError:
                print('Incorrect format')
        return right_answers


class SquaresCalculator():

    def __init__(self):
        self.result = None
        self.x = random.randint(11, 29)
        print(self.x)

    def calculate(self):
        self.result = pow(self.x, 2)

    def answer(self, right_answers):
        while True:
            answer = input()
            try:
                answer = float(answer)
                if answer == self.result:
                    print('Right!')
                    right_answers += 1
                    break
                else:
                    print('Wrong!')
                    break
            except ValueError:
                print('Incorrect format')
        return right_answers


if __name__ == '__main__':
    right_answers = 0
    while True:
        difficult = input('''Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29\n''')
        if difficult == '1':
            difficult += ' (simple operations with numbers 2-9)'
            for i in range(5):
                calculator = Calculator()
                calculator.calculate()
                right_answers = calculator.answer(right_answers)
            print(f'Your mark is {right_answers}/5.')
            break
        elif difficult == '2':
            difficult += ' (integral squares of 11-29)'
            for i in range(5):
                calculator = SquaresCalculator()
                calculator.calculate()
                right_answers = calculator.answer(right_answers)
            print(f'Your mark is {right_answers}/5.')
            break
        else:
            print('Incorrect format.')
            continue
    saving = input('Would you like to save your result to the file? Enter yes or no.\n')
    if saving in ['yes', 'YES', 'y', 'Yes']:
        name = input('What is your name?\n')
        with open('results.txt', 'a') as file:
            file.write(f'{name}: {right_answers}/5 in level {difficult}.\n')
        print('The results are saved in "results.txt".')
    else:
        pass
