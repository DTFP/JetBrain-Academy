import random

list_of_words = ['python', 'java', 'swift', 'javascript']
print('H A N G M A N')
losses = 0
wins = 0
game = True

while game:
    word = random.choice(list_of_words)
    new_word_list = list('-' * len(word))
    number_of_attempt = 8
    used_letters = list()
    action = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if action == 'results':
        print(f'You won: {wins} times.')
        print(f'You lost: {losses} times.')
        continue
    elif action == 'exit':
        break
    elif action == 'play':
        print()
        print(''.join(new_word_list))
        while number_of_attempt > 0:
            while True:
                guess = input('Input a letter:')
                if len(guess) > 1 or len(guess) == 0:
                    print('Please, input a single letter.\n')
                    print(''.join(new_word_list))
                    continue
                if not guess.isalpha() or not guess.islower():
                    print('Please, enter a lowercase letter from the English alphabet.\n')
                    print(''.join(new_word_list))
                    continue
                if guess in used_letters:
                    print("You've already guessed this letter.\n")
                    print(''.join(new_word_list))
                    continue
                else:
                    break
            if guess not in word:
                print("That letter doesn't appear in the word.\n")
                print(''.join(new_word_list))
                number_of_attempt -= 1
                used_letters.append(guess)
                continue
            elif guess in word:
                for i in range(len(word)):
                    if guess == word[i]:
                        new_word_list[i] = guess
                new_word = ''.join(new_word_list)
                used_letters.append(guess)
                print()
                print(''.join(new_word_list))
            if '-' not in new_word_list:
                print(f'You guessed the word {word}!')
                print('You survived!')
                wins += 1
                break
    if '-' in new_word_list:
        print('You lost!')
        losses += 1
        continue


