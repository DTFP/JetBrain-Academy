class CoffeeMachine:

    def __init__(self, money, water, milk, coffee, cups):
        self.money = int(money)
        self.water = int(water)
        self.milk = int(milk)
        self.coffee = int(coffee)
        self.cups = int(cups)

    def __str__(self):
        return f'''The coffee machine has:
{self.water} ml of water
{self.milk} ml of milk
{self.coffee} g of coffee beans
{self.cups} disposable cups
${self.money} of money'''

    def buy(self, type):
        self.type = type
        if type == 'back':
            pass
        elif type == '1':
            if self.water >= 250 and self.coffee >= 16 and self.cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.coffee -= 16
                self.money += 4
                self.cups -= 1
            else:
                if self.water < 250:
                    print('Sorry, not enough water!')
                if self.coffee < 16:
                    print('Sorry, not enough coffee!')
                if self.cups < 1:
                    print('Sorry, not enough disposable cups!')
        elif type == '2':
            if self.water >= 350 and self.milk >= 75 and self.coffee >= 20 and self.cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.money += 7
                self.cups -= 1
            else:
                if self.water < 350:
                    print('Sorry, not enough water!')
                if self.milk < 75:
                    print('Sorry, not enough milk!')
                if self.coffee < 20:
                    print('Sorry, not enough coffee!')
                if self.cups < 1:
                    print('Sorry, not enough disposable cups!')
        elif type == '3':
            if self.water >= 200 and self.milk >= 100 and self.coffee >= 12 and self.cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.money += 6
                self.cups -= 1
            else:
                if self.water < 200:
                    print('Sorry, not enough water!')
                if self.milk < 100:
                    print('Sorry, not enough milk!')
                if self.coffee < 12:
                    print('Sorry, not enough coffee!')
                if self.cups < 1:
                    print('Sorry, not enough disposable cups!')

    def fill(self):
        water = int(input('Write how many ml of water you want to add:\n'))
        milk = int(input('Write how many ml of milk you want to add: \n'))
        coffee = int(input('Write how many grams of coffee beans you want to add:\n'))
        cups = int(input('Write how many disposable cups you want to add: \n'))
        self.water += int(water)
        self.coffee += int(coffee)
        self.milk += int(milk)
        self.cups += int(cups)

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0


if __name__ == '__main__':
    machine = CoffeeMachine(550, 400, 540, 120, 9)
    while True:
        print('Write action (buy, fill, take, remaining, exit):')
        action = input()
        print()
        if action == 'buy':
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            type = input()
            machine.buy(type)
            print()
        elif action == 'fill':
            machine.fill()
            print()
        elif action == 'take':
            machine.take()
            print()
        elif action == 'remaining':
            print(machine, '\n')
        elif action == 'exit':
            break
