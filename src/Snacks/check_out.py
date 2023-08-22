import re

import datetime as datetime

storeName ="SEMICOLON STORE"
Branch = "MAIN BRANCH"
Address = "312, HERBERT MACAULAY WAY, SABO YABA, LAGOS STATE."
number = "+2348345689034"
datetime = datetime.datetime.now
customerName = " "
product = []
productNumber = []
productNumberAmount = []
totalProductNumber = []
moreItems = " "
discountInput = 0
cashierDetails = " "




def customer_name_entry():
    global customerName
    name = input("What is customer name: ")
    if re.search("^(?!$)\D+$",name):
        var = customerName == name
        list_of_items()

    else:
        print("invalid ")
        customer_name_entry()

def list_of_items():
    global product
    items = input("what did user buy? ")
    if re.search("^(?!$)\D+$", items):
        product.append(items)
        unit_of_items()
    else:
        print('Invalid entry')
        list_of_items()

def unit_of_items():
    global productNumber
    number_of_items = input("How many pieces? ")

    if number_of_items.isdigit():
        productNumber.append(int(number_of_items))
        unit_per_items_amount()

    else:
        print("invalid entry")
        unit_of_items()

def unit_per_items_amount():
    global productNumberAmount
    amount = input("How much per unit? ")
    if amount.isdigit():
        productNumberAmount.append(int(amount))
        add_more_items()

    else:
        print("Invalid amount")
        unit_per_items_amount()

def add_more_items():
    global moreItems
    addItems = input("Add more items? ")
    if re.search("^(?!$)\D+$", addItems):
        if addItems.casefold()=="yes":
             list_of_items()
        elif  addItems.casefold()=="no":
            cashier_details()


    else:
        print("invalid entry")
        cashier_details()


def cashier_details():
    global cashierDetails
    details = input("What is your name: ")
    if re.search("^(?!$)\D+$", details):
        var = cashierDetails == details
        discount()
    else:
        print("Invalid Entry")
        cashier_details()

def discount():
    global discountInput
    discounted = int(input("How much discount will the customer get? "))
    if discounted >=0 or discounted <= 100:
        save_details()
    else:
        print("Enter value between 1 and 100")
        discount()

def save_details():
    global cashierDetails
    global customerName

    print(f"\n {storeName}\n{Branch}\nLocation: {Address}\n Tel: {number}\nDate: {datetime}\ncashier: {cashierDetails}\n Customer Name: {customerName} ")
    receiptHead()


def receiptHead():
    global discountInput, totalProductNumber
    print(f"""\n{"=" *  60}\n\t ITEM \tQTY    PRICE \t\tTOTAL(NGN)\n{"-" * 60}""")
    num = 0
    subTotal = 0.0

    for row in range(len(product)):
        num = productNumber[row] * productNumberAmount[row]
        totalProductNumber.append(num)

    subTotal += num
    for row in range(len(product)):
        print(f"""
        {product[row]:<10}{productNumber[row]:10}{productNumberAmount[row]:<14.2f} {totalProductNumber[row]:<14.2f}""")
        newDiscount = subTotal * (discounted/100)
        vat = subTotal * 0.175
        bill = subTotal + vat - newDiscount

        print(f"""{"-" * 60} \n\t\t\t\t Sub Total: {subTotal:.2f} \n\t\t\t\t Discount:{newDiscount:.2f}\n\t\t\t\t VAT @17.50: {vat:.2f} 
        \n{"=" * 60}\n\t\t\t\t Bill Total: {bill:.2f}\n{"=" *60 }\n\t THIS IS NOT A RECEIPT KINDLY PAY {bill:.2f}\n{"=" * 60}
        """)



if __name__ == '__main__':
    customer_name_entry()

