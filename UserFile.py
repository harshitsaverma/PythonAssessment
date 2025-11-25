'''
This is for assessment to create file as per user inputs.
'''

Content = input('Enter text to write to the file: ')
with open('output.txt','wt') as file:
    file.write(f'{Content}\n')
    print('Data successfully written to output.txt.')

Content2 = input('Enter additional text to append: ')
with open('output.txt','at') as file:
    file.write(f'{Content2}\n')
    print('Data successfully appended.')
    print('============================')

with open('output.txt','rt') as file:
    print('Final content of output.txt:')
    print(file.read())

