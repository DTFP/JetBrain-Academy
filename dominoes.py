import random


def generate_set():
    """
    :return: set of dominoes
    """
    generated_set = []
    for i in range(0, 7):
        for j in range(6, i-1, -1):
            generated_set.append([i, j])
    return generated_set


def split_set(set_):
    """
    :param set_: dominoes set
    :return: shuffled players' sets, stock
    """
    random.shuffle(set_)
    first_player_set = []
    second_player_set = []
    for _ in range(7):
        piece = random.choice(set_)
        first_player_set.append(piece)
        set_.remove(piece)
    for _ in range(7):
        piece = random.choice(set_)
        second_player_set.append(piece)
        set_.remove(piece)
    stock = set_
    return first_player_set, second_player_set, stock


def determine_first_player(set1, set2):
    """
    :param set1: player set
    :param set2: computer set
    :return: set1, set2, domino snake, who is going 1st
    """
    max1 = [-1, -1]
    for i in range(len(set1)):
        if set1[i][0] == set1[i][1]:
            if set1[i][0] > max1[0]:
                max1 = set1[i]
    max2 = [-1, -1]
    for i in range(len(set2)):
        if set2[i][0] == set2[i][1]:
            if set2[i][0] > max2[0]:
                max2 = set2[i]
    if max1[0] > max2[0]:
        first_domino = [max1]
        set1.remove(first_domino[0])
        first_player = 'computer'
    elif max1[0] < max2[0]:
        first_domino = [max2]
        set2.remove(first_domino[0])
        first_player = 'player'
    return set1, set2, first_domino, first_player


def game_start():
    full_domino_set = generate_set()
    domino_snake = 0
    while domino_snake == 0:
        player_pieces, computer_pieces, stock_pieces = split_set(full_domino_set)
        player_pieces, computer_pieces, domino_snake, status = \
            determine_first_player(player_pieces, computer_pieces)

    return player_pieces, computer_pieces, stock_pieces, domino_snake, status


def player_command():
    while True:
        command = input()
        try:
            command = int(command)
        except ValueError:
            print('Invalid input. Please try again.')
            continue
        if abs(int(command)) > len(player_pieces):
            print('Invalid input. Please try again.')
            continue
        else:
            break
    return command


def main_print():
    print('=' * 70)
    print(f'Stock size: {len(stock_pieces)}')
    print(f'Computer pieces: {len(computer_pieces)}\n')
    if len(domino_snake) <= 6:
        for i in range(len(domino_snake)):
            print(domino_snake[i], end='')
    else:
        for i in range(3):
            print(domino_snake[i], end='')
        print('...', end='')
        for i in range(-3, 0, 1):
            print(domino_snake[i], end='')
    print()
    print()


def print_player_pieces():
    print('Your pieces:')
    for i in range(0, len(player_pieces)):
        print(f'{i+1}:{player_pieces[i]}')
    print()


def player_turn():
    while True:
        command = player_command()
        if int(command) < 0:
            if domino_snake[0][0] in player_pieces[abs(command)-1]:
                if player_pieces[abs(command)-1][0] == domino_snake[0][0]:
                    player_pieces[abs(command)-1][0], player_pieces[abs(command)-1][1] = \
                            player_pieces[abs(command)-1][1], player_pieces[abs(command)-1][0]
                    domino_snake.insert(0, player_pieces.pop(abs(command) - 1))
                    break
                elif domino_snake[0][0] == player_pieces[abs(command)-1][1]:
                    domino_snake.insert(0, player_pieces.pop(abs(command) - 1))
                break
            else:
                print('Illegal move. Please try again.')
                continue
        elif int(command) == 0:
            if len(stock_pieces) > 0:
                player_pieces.append(stock_pieces.pop())
                break
            else:
                break
        elif int(command) > 0:
            if domino_snake[-1][1] == player_pieces[command-1][1]:
                player_pieces[command-1][0], player_pieces[command-1][1] = \
                        player_pieces[command-1][1], player_pieces[command-1][0]
                domino_snake.append(player_pieces.pop(command - 1))
                break
            elif domino_snake[-1][1] == player_pieces[command-1][0]:
                domino_snake.append(player_pieces.pop(command - 1))
                break
            else:
                print('Illegal move. Please try again.')
                continue
    return player_pieces, domino_snake, stock_pieces


def computer_turn():

    # checking possible dominoes for this turn
    available_pieces = []
    for piece in computer_pieces:
        if domino_snake[0][0] in piece or domino_snake[-1][1] in piece:
            available_pieces.append(piece)
    if len(available_pieces) == 0 and len(stock_pieces) > 0:
        computer_pieces.append(stock_pieces.pop())
    elif len(available_pieces) == 0 and len(stock_pieces) == 0:
        pass
    else:
        turn = computer_analysis(available_pieces,domino_snake)
        computer_pieces.remove(turn)
        if domino_snake[0][0] in turn:
            if domino_snake[0][0] == turn[0]:
                turn[0], turn[1] = turn[1], turn[0]
                domino_snake.insert(0, turn)
            elif domino_snake[0][0] == turn[1]:
                domino_snake.insert(0, turn)
        elif domino_snake[-1][1] in turn:
            if domino_snake[-1][1] == turn[1]:
                turn[0], turn[1] = turn[1], turn[0]
                domino_snake.append(turn)
            elif domino_snake[-1][1] == turn[0]:
                domino_snake.append(turn)

    return computer_pieces, domino_snake, stock_pieces


def draw_condition(domino_snake):
    """
    :param domino_snake: current gameboard
    :return: True/False - is it draw?
    """
    count = 0
    if domino_snake[0][0] == domino_snake[-1][1]:
        for i in range(len(domino_snake)):
            for j in range(2):
                if domino_snake[i][j] == domino_snake[0][0]:
                    count += 1
        if count == 8:
            return True
        else:
            count = 0
    else:
        return False


def computer_analysis(available_set, domino_snake):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    for i in range(len(available_set)):
        count_0 += available_set[i].count(0)
        count_1 += available_set[i].count(1)
        count_2 += available_set[i].count(2)
        count_3 += available_set[i].count(3)
        count_4 += available_set[i].count(4)
        count_5 += available_set[i].count(5)
        count_6 += available_set[i].count(6)
    for i in range(len(domino_snake)):
        count_0 += domino_snake[i].count(0)
        count_1 += domino_snake[i].count(1)
        count_2 += domino_snake[i].count(2)
        count_3 += domino_snake[i].count(3)
        count_4 += domino_snake[i].count(4)
        count_5 += domino_snake[i].count(5)
        count_6 += domino_snake[i].count(6)
    count = {0:count_0, 1: count_1, 2: count_2, 3: count_3, 4:count_4, 5:count_5, 6:count_6}
    maximum_score = 0
    turn = -1
    for piece in available_set:
        if count[piece[0]] + count[piece[1]] > maximum_score:
            turn = piece
    return turn


player_pieces, computer_pieces, stock_pieces, domino_snake, status = game_start()

while True:
    main_print()
    print_player_pieces()
    if len(player_pieces) == 0:
        print('Status: The game is over. You won!')
        break
    if len(computer_pieces) == 0:
        print('Status: The game is over. The computer won!')
        break
    if draw_condition(domino_snake):
        print("Status: The game is over. It's a draw!")
        break
    if status == 'player':
        print("Status: It's your turn to make a move. Enter your command.")
        player_pieces, domino_snake, stock_pieces = player_turn()
        status = 'computer'
        continue
    elif status == 'computer':
        print(input('Status: Computer is about to make a move. Press Enter to continue...'))
        computer_pieces, domino_snake, stock_pieces = computer_turn()
        status = 'player'
        continue
