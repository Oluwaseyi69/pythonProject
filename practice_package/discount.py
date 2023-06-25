price = int(input("Enter a Price: "))
credit_score = int(input("Enter a Credit Score: "))

if credit_score < 2:
    discount = price * (10/100)
    new_price = price - discount
    down_payment = price * (10/100)
    print(f"""
    You have a good Credit Score!!!,  
    You have been offered 10% discount. 
    Your Discounted price :                    {new_price}
    You can make a Down Payment:               {down_payment}
    """)
else:
    down_payment = price * (25/100)
    new_price = price - down_payment
    print("you do not have discount, and will pay 25% down payment of: ", down_payment)