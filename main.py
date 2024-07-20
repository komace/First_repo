fruit = 'apple'
for char in fruit:
    print (char, end = " ")

odd_numbers = [1,2,3,4]
for i in odd_numbers:
    print(i **3, end = " \ ")



user_input = input("enter number:")
total_chars = len(user_input)
space_count = 0
for char in user_input:
        if char == " ":
            space_count += 1

print(f'Total Chars in : {total_chars}')
print(f"Count of spaces : {space_count}")