# here is while loop examples

while True:
    print('Whats up')

name = ''

while len(name) == 0:
    name = input('what is your name: ')

print('hey '+name)

name = None

while not name:
    name = input('whats ur name: ')

print('hey '+name)