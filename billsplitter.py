import random


class BillSplitter:

    def __init__(self):
        self.num_people = int(input('Enter the number of friends joining (including you):\n'))
        if self.num_people > 0:
            print('Enter the name of every friend (including you), each on a new line:')
            self.names = {input(): 0 for _ in range(self.num_people)}
            self.bill = int(input('\nEnter the total bill value:\n'))
            self.lucky_guy()
            self.split_bill()
        elif self.num_people <= 0:
            print('No one is joining for the party')
            exit()

    def lucky_guy(self):
        self.use = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if self.use == 'Yes':
            self.lucky = random.choice(list(self.names.keys()))
            print(f'{self.lucky} is the lucky one!')
        else:
            print('No one is going to be lucky')

    def split_bill(self):
        if self.use == 'Yes':
            each_bill = round(self.bill / (self.num_people - 1), 2)
            self.names = {names: each_bill for names in self.names}
            self.names[self.lucky] = 0
        else:
            each_bill = round(self.bill / self.num_people, 2)
            self.names = {names: each_bill for names in self.names}
        print(self.names)


if __name__ == '__main__':
    bill = BillSplitter()
