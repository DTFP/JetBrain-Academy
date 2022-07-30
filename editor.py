class MarkdownEditor:

    def __init__(self):
        self.formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line',
                           'ordered-list', 'unordered-list', '!done']
        self.user_help = 'Available formatters: plain bold italic header link inline-code new-line'
        self.output = []

    def plain(self):
        self.text = input('Text: ')
        self.plain_text = self.text
        self.output.append(self.plain_text)

    def bold(self):
        self.text = input('Text: ')
        self.bold_text = f'**{self.text}**'
        self.output.append(self.bold_text)

    def italic(self):
        self.text = input('Text: ')
        self.italic_text = f'*{self.text}*'
        self.output.append(self.italic_text)

    def inline_code(self):
        self.text = input('Text: ')
        self.inlice_code_text = f'`{self.text}`'
        self.output.append(self.inlice_code_text)

    def link(self):
        self.text = input('Label: ')
        self.url = input('URL: ')
        self.link_text = f'[{self.text}]({self.url})'
        self.output.append(self.link_text)

    def header(self):
        while True:
            self.level = int(input('Level: '))
            if not (1 <= self.level <= 6):
                print('The level should be within the range of 1 to 6')
                continue
            else:
                break
        self.n = self.level * '#'
        self.text = input('Text: ')
        self.header_text = f'{self.n} {self.text}\n'
        self.output.append(self.header_text)

    def new_line(self):
        self.text = '\n'
        self.output.append(self.text)

    def ordered_list(self):
        while True:
            self.n = int(input('Number of rows: '))
            if self.n <= 0:
                print('The number of rows should be greater than zero')
                continue
            else:
                break
        self.text = []
        for i in range(1, self.n + 1):
            self.text = f'{i}. ' + input() + '\n'
            self.output.append(self.text)

    def unordered_list(self):
        while True:
            self.n = int(input('Number of rows: '))
            if self.n <= 0:
                print('The number of rows should be greater than zero')
                continue
            else:
                break
        self.text = []
        for _ in range(self.n):
            self.text = '*' + input() + '\n'
            self.output.append(self.text)

    def save(self):
        with open('output.md', 'w') as file:
            file.write(''.join(editor.output))


if __name__ == '__main__':
    editor = MarkdownEditor()
    while True:
        user_choice = input('Choose a formatter: ')
        if user_choice not in editor.formatters:
            print('Unknown formatting type or command')
            continue
        else:
            if user_choice == 'plain':
                editor.plain()
                print(''.join(editor.output))
                continue
            elif user_choice == 'bold':
                editor.bold()
                print(''.join(editor.output))
                continue
            elif user_choice == 'ordered-list':
                editor.ordered_list()
                print(''.join(editor.output))
                continue
            elif user_choice == 'unordered-list':
                editor.unordered_list()
                print(''.join(editor.output))
                continue
            elif user_choice == 'italic':
                editor.italic()
                print(''.join(editor.output))
                continue
            elif user_choice == 'header':
                editor.header()
                print(''.join(editor.output))
                continue
            elif user_choice == 'link':
                editor.link()
                print(''.join(editor.output))
                continue
            elif user_choice == 'new-line':
                editor.new_line()
                print(''.join(editor.output))
                continue
            elif user_choice == 'inline-code':
                editor.inline_code()
                print(''.join(editor.output))
                continue
            elif user_choice == '!done':
                editor.save()
                break
