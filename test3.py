with open("test.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open("test.txt", "r") as fh:
    lines = [prere.strip() for prere in fh.readlines()]

print(lines)

byte_str = 'some text'.encode()
print(byte_str)