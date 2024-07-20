fh = open('test.txt', 'w')
fh.write('first line\nsecond linethird line')
fh.close()

fh = open('test.txt', 'r')
while True:
    line = fh.readline()
    if  line:
        break
    print(line)

fh.close()