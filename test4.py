# Перетворення списку чисел у байт-рядок
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)  # Виведе байтове представлення чисел


print(b'Hello world!'.decode('utf-16'))

s = "періоньвглгвл!"

utf8 = s.encode()
print(f"UTF-8: {utf8}")


utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)

message = "Hello world!"
message[0]