# write your code here
state = '         '

counter_x = 0
counter_o = 0
counter_empty = 9
x_win_counter = 0
o_win_counter = 0

state_list = [[state[0], state[1], state[2]],
              [state[3], state[4], state[5]],
              [state[6], state[7], state[8]]]

def print_state (matrix):
    print(f"""---------
| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |
| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |
| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |
---------""")

print_state(state_list)

while counter_empty > 0:
    user1_input = input()
    x1 = user1_input[0]
    x2 = user1_input[2]
    try:
        x1, x2 = int(x1), int(x2)
    except ValueError:
        print('You should enter numbers!')
        continue
    else:
        if (x1 < 1 or x1 > 3) or (x2 < 1 or x2 > 3):
            print('Coordinates should be from 1 to 3')
            continue
        elif state_list[x1-1][x2-1] != ' ':
            print('This cell is occupied! Choose another one!')
            continue
        else:
            state_list[x1-1][x2-1] = 'X'
            counter_empty -= 1
            print_state(state_list)
            # Check the game state
            # check 1st column
            if state_list[0][0] == state_list[1][0] == state_list[2][0] == 'X':
                x_win_counter += 1
                break
            # check 2nd column
            if state_list[0][1] == state_list[1][1] == state_list[2][1] == 'X':
                x_win_counter += 1
                break
            # check 3rd column
            if state_list[0][2] == state_list[1][2] == state_list[2][2] == 'X':
                x_win_counter += 1
                break
            # check 1st row
            if state_list[0][0] == state_list[0][1] == state_list[0][2] == 'X':
                x_win_counter += 1
                break
            # check 2nd row
            if state_list[1][0] == state_list[1][1] == state_list[1][2] == 'X':
                x_win_counter += 1
                break
            # check 3rd row
            if state_list[2][0] == state_list[2][1] == state_list[2][2] == 'X':
                x_win_counter += 1
                break
            # check 1st diagonal
            if state_list[0][0] == state_list[1][1] == state_list[2][2] == 'X':
                x_win_counter += 1
                break
            # check 2nd diagonal
            if state_list[2][0] == state_list[1][1] == state_list[0][2] == 'X':
                x_win_counter += 1
                break
    if counter_empty > 0:
        Flag = True
        while Flag:
            user2_input = input()
            x1 = user2_input[0]
            x2 = user2_input[2]
            try:
                x1, x2 = int(x1), int(x2)
            except ValueError:
                print('You should enter numbers!')
                continue
            else:
                if (x1 < 1 or x1 > 3) or (x2 < 1 or x2 > 3):
                    print('Coordinates should be from 1 to 3')
                    continue
                elif state_list[x1-1][x2-1] != ' ':
                    print('This cell is occupied! Choose another one!')
                    continue
                else:
                    state_list[x1-1][x2-1] = 'O'
                    Flag = False
                    counter_empty -= 1
                    print_state(state_list)
                    # Check the game state
                    # check 1st column
                    if state_list[0][0] == state_list[1][0] == state_list[2][0] == 'O':
                        o_win_counter += 1
                        break
                    # check 2nd column
                    if state_list[0][1] == state_list[1][1] == state_list[2][1] == 'O':
                        o_win_counter += 1
                        break
                    # check 3rd column
                    if state_list[0][2] == state_list[1][2] == state_list[2][2] == 'O':
                        o_win_counter += 1
                        break
                    # check 1st row
                    if state_list[0][0] == state_list[0][1] == state_list[0][2] == 'O':
                        o_win_counter += 1
                        break
                    # check 2nd row
                    if state_list[1][0] == state_list[1][1] == state_list[1][2] == 'O':
                        o_win_counter += 1
                        break
                    # check 3rd row
                    if state_list[2][0] == state_list[2][1] == state_list[2][2] == 'O':
                        o_win_counter += 1
                        break
                    # check 1st diagonal
                    if state_list[0][0] == state_list[1][1] == state_list[2][2] == 'O':
                        o_win_counter += 1
                        break
                    # check 2nd diagonal
                    if state_list[2][0] == state_list[1][1] == state_list[0][2] == 'O':
                        o_win_counter += 1
                        break
# check winner
if x_win_counter > 0:
    print('X wins')
elif o_win_counter > 0:
    print('O wins')
else:
    print('Draw')
