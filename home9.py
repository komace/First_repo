def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)
    apply_discount() 
    return price
price1 = float(input("enter : ")) 
discount = float(input("Enter :")) /100
final_price = discount_price(price1, discount)
print(f"sa: {final_price}")