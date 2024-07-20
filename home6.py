pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool / quantity
    chunk = int(chunk)
    print("ty lox")
except :
    print('Divide by zero completed!')
    pass