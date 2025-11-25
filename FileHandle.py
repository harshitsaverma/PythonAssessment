'''
This is for assessment of file handling. Below command to create sample file.
with open('sample.txt', 'wt') as file:
    file.write('This is a sample file.\nIt contains multiple lines.')
'''
try:
    with open('sample.txt','rt') as file:
        Line1 = file.readline()
        Line2 = file.readline()
except FileNotFoundError as err:
    print('The file ''sample.txt'' not found')
else:
    print('Reading file content:')
    print(f'Line1: {Line1}')
    print(f'Line2: {Line2}')
