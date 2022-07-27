import random
from io import StringIO
import argparse

parser = argparse.ArgumentParser(description='This program help you to learn some terms')

parser.add_argument('--import_from', help='import cards from file')
parser.add_argument('--export_to', help='export cards to file')
args = parser.parse_args()


def comparison(string1, string2):
    """
    :param string1:
    :param string2:
    :return: boolean comparison result of
            string1 and string2
    """
    if string1 == string2:
        return True
    else:
        return False


def check_term(dict_card, term):
    """
    :param dict_card: dict. {term:[definition, wrong_answers]}
    :param term: string, term
    :return: term that is not in dict.
    """
    while term in dict_card:
        print(f'The term "{term}" already exists. Try again:')
        buffer.write(f'The term "{term}" already exists. Try again:\n')
        term = input()
        buffer.write(term + '\n')
    return term


def check_definition(dict_card, definition):
    """
    :param dict_card: dict. {term:[definition, wrong_answers]}
    :param definition: string
    :return: definition that is not in dict.
    """
    values = ''
    for value in dict_card.values():
        values += str(value)
    while definition in values:
        print(f'The definition "{definition}" already exists. Try again:')
        buffer.write(f'The definition "{definition}" already exists. Try again:\n')
        definition = input()
        buffer.write(definition + '\n')
    return definition


def add_cards(dict_card):
    """
    :param dict_card: dictionary {term:[definition, wrong_answers]}
    :return: dictionary with added card
    """
    print('The card:')
    buffer.write('The card:\n')
    term = input()
    buffer.write(term + '\n')
    term = check_term(dict_card, term)
    print('The definition of the card:')
    buffer.write('The definition of the card:\n')
    definition = input()
    buffer.write(definition + '\n')
    definition = check_definition(dict_card, definition)
    mistakes = 0
    dict_card[term] = [definition, mistakes]
    print(f'The pair ("{term}":"{definition}") has been added.\n')
    buffer.write(f'The pair ("{term}":"{definition}") has been added.\n')
    return dict_card


def remove_card(dict_card):
    """
    :param dict_card: dictionary {term:[definition, wrong_answers]}
    :return: dictionary without deleted term
    """
    print('Which card?')
    buffer.write('Which card?')
    term = input()
    buffer.write(term + '\n')
    if term in dict_card:
        del dict_card[term]
        print('The card has been removed.\n')
        buffer.write('The card has been removed.\n')
    else:
        print("Can't remove " + f'"{term}"' + ": there is no such card.\n")
        buffer.write("Can't remove " + f'"{term}"' + ": there is no such card.\n")
    return dict_card


def import_card(dict_card):
    """
    import card from a file (term definition wrong_answers\n)
    :param dict_card: dictionary
    :return: updated dictionary
    """
    print('File name:')
    buffer.write('File name:\n')
    file = input()
    buffer.write(file + '\n')
    try:
        opened_file = open(file, 'r')
        n = 0
        for line in opened_file.readlines():
            term = str(line[0:line.index(' ')])
            if term in dict_card:
                dict_card.pop(term)
            definition_index = line.index(' ') + 1
            wrong_answers_index = line.rindex(' ') + 1
            definition = str(line[definition_index:wrong_answers_index - 1])
            wrong_answers = int(str(line[wrong_answers_index: -1]))
            dict_card[term] = [definition, wrong_answers]
            n += 1
        print(f'{n} cards have been loaded.')
        buffer.write(f'{n} cards have been loaded.\n')
        opened_file.close()
    except FileNotFoundError:
        print('File not found.')
        buffer.write('File not found.\n')
    return dict_card


def export_cards(dict_card):
    """
    export dictionary to a file (term definition wrong_answers\n)
    :param dict_card: dictionary
    :return:
    """
    print('File name:')
    buffer.write('File name:\n')
    file = open(input(), 'a', encoding='utf-8')
    if file is None:
        file = open(args.export_to, 'a', encoding='utf-8')
    for term in dict_card:
        file.write(f'{term} {dict_card[term][0]} {dict_card[term][1]}\n')
    file.close()
    print(f'{len(dict_card)} cards have been saved.')
    buffer.write(f'{len(dict_card)} cards have been saved.\n')


def check_knowledge(dict_card):
    """
    :param dict_card: {term:[definition, wrong_answers]}
    :return: correct/incorrect answer
    """
    print('How many times to ask?')
    buffer.write('How many times to ask?\n')
    n = int(input())
    buffer.write(str(n) + '\n')
    for i in range(n):
        term, [definition, wrong_answers] = random.choice(list(dict_card.items()))
        print(f'Print the definition of "{term}":')
        buffer.write(f'Print the definition of "{term}":\n')
        guess = input()
        buffer.write(guess + '\n')
        if comparison(guess, definition):
            print('Correct!')
            buffer.write('Correct!\n')
        else:
            wrong_answers += 1
            dict_card[term] = [definition, wrong_answers]
            values = ''
            for value in dict_card.values():
                values += str(value)
            if guess in values:
                for all_terms, [all_definitions, all_wrong_answers] in dict_card.items():
                    if all_definitions == guess:
                        print(
                            f'Wrong. The right answer is "{definition}", but your definition is correct for "{all_terms}".')
                        buffer.write(
                            f'Wrong. The right answer is "{definition}", but your definition is correct for "{all_terms}".\n')
            else:
                print(f'Wrong. The right answer is "{definition}".')
                buffer.write(f'Wrong. The right answer is "{definition}".\n')
    return dict_card


def hardest_card(dict_card):
    """
    :param dict_card: dict_card: {term:[definition, wrong_answers]}
    :return: term with maximum number of wrong_answers
    """
    maximum = 1
    term = []
    for card in dict_card:
        if dict_card[card][1] > maximum:
            term.clear()
            term.append(card)
            maximum = dict_card[card][1]
        elif dict_card[card][1] == maximum:
            term.append(card)
    if len(term) == 1:
        print(f'The hardest card is "{term[0]}". You have {maximum} errors answering it.')
        buffer.write(f'The hardest card is "{term[0]}". You have {maximum} errors answering it.\n')
    elif len(term) > 1:
        term = '", "'.join(term)
        print(f'The hardest cards are "{term}". You have {maximum} errors answering them.')
        buffer.write(f'The hardest cards are "{term}". You have {maximum} errors answering them.\n')
    else:
        print('There are no cards with errors.')
        buffer.write('There are no cards with errors.\n')


def reset_stats(dict_card):
    for term in dict_card:
        dict_card[term][1] = 0
    print('Card statistics have been reset')
    buffer.write('Card statistics have been reset\n')
    return dict_card


def log_function():
    print("File name:")
    buffer.write("File name:\n")
    filename = input()
    buffer.write(filename + '\n')
    content = buffer.getvalue().split('\n')
    with open(filename, 'w') as file:
        for line in content:
            print(line, file=file)
    print('The log has been saved.')
    buffer.write("The log has been saved.\n")


def saving(dict_card):
    file = open(args.export_to, 'a', encoding='utf-8')
    for term in dict_card:
        file.write(f'{term} {dict_card[term][0]} {dict_card[term][1]}\n')
    file.close()
    print(f'{len(dict_card)} cards have been saved.')
    buffer.write(f'{len(dict_card)} cards have been saved.\n')


def importing(dict_card):
    try:
        opened_file = open(args.import_from, 'r')
        n = 0
        for line in opened_file.readlines():
            term = str(line[0:line.index(' ')])
            if term in dict_card:
                dict_card.pop(term)
            definition_index = line.index(' ') + 1
            wrong_answers_index = line.rindex(' ') + 1
            definition = str(line[definition_index:wrong_answers_index - 1])
            wrong_answers = int(str(line[wrong_answers_index: -1]))
            dict_card[term] = [definition, wrong_answers]
            n += 1
        print(f'{n} cards have been loaded.')
        buffer.write(f'{n} cards have been loaded.\n')
        opened_file.close()
    except FileNotFoundError:
        print('File not found.')
        buffer.write('File not found.\n')
    return dict_card


buffer = StringIO()
dictionary = {}
if args.import_from:
    dictionary = importing(dictionary)
while True:
    print('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):')
    buffer.write('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n')
    action = input()
    buffer.write(action + '\n')
    if action == 'add':
        dictionary = add_cards(dictionary)
    elif action == 'remove':
        dictionary = remove_card(dictionary)
    elif action == 'export':
        export_cards(dictionary)
    elif action == 'import':
        dictionary = import_card(dictionary)
    elif action == 'ask':
        check_knowledge(dictionary)
    elif action == 'log':
        log_function()
    elif action == 'hardest card':
        hardest_card(dictionary)
    elif action == 'reset stats':
        dictionary = reset_stats(dictionary)
    elif action == 'exit':
        if args.export_to:
            saving(dictionary)
        print('Bye bye!')
        buffer.write('Bye bye!\n')
        break
print(dictionary)
