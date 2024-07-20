num = int(input('Enter a number:'))
if num > 0 :
    if num % 2 == 0:
        result = "positive odd number"
        print(result)
    else:
        result = "positive even number"
        print(result)    
elif num < 0:
    result = "negative number"
    print(result)
else:
    result = "It is zero"
    print(result)    
