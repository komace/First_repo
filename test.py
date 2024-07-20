fh = open('test.txt', 'w')
fh.write('hello!hello!')
fh.close()

fh = open('test.txt', 'r')
while True:
    symbol = fh.read(2)
    if len(symbol) == 0:
        break
    print(symbol)

fh.close()
