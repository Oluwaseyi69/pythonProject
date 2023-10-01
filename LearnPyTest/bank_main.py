# import bank
import re

# from LearnPyTest.bank import Bank

from LearnPyTest.bank import Bank

first_name = []
last_name = []
pin = []


def welcome():
    print("Welcome to Shebotimo Bank")
    display()


def display():
    print("""
        1-> Create Account
        2-> Deposit 
        3-> Withdraw
        4-> Check Balance
        5-> Exit
    """)
    user_input = input("Kindly enter a number: ")
    if user_input == "1":
        create_account()
    elif user_input == "2":
        deposit_cash()
    elif user_input == "3":
        withdraw_cash()
    elif user_input == "4":
        check_balance()
    elif user_input == "5":
        print(f"""
            #############@@@@@@@@@@@@@@@@@@@@############
                Thank you for choosing Shebotimo Bank
            #############@@@@@@@@@@@@@@@@@@@@############
            """)
        exit()


def create_account():
    first_name_entered()
    last_name_entered()
    pin_entered()


def first_name_entered():
    global first_name
    first_name = input("Enter Your First Name:: ")
    if re.search(r"[a-zA-Z]+", first_name):
        last_name_entered()
    else:
        print("kindly input alphabets only")
        first_name_entered()


def last_name_entered():
    global last_name
    last_name = input("Enter your Last Name:: ")
    if re.search(r"[a-zA-Z]+", last_name):
        pin_entered()
    else:
        print("kindly input alphabets only")
        last_name_entered()


def pin_entered():
    global pin
    pin = input("Enter your pin:: ")
    if re.search(r"[a-zA-Z]+", pin):
        show_info()

    show_info()


def show_info():
    account_created = bank.register(first_name, last_name, pin)
    account = account_created.accountNumber
    print(f"""
            ************************************************
                    Welcome to Shebotimo bank,
                    Account Successfully Created
                    Account name:  {first_name} {last_name}
                    Account number: {account}
            ************************************************
                    Thank you for Banking with us.
            ************************************************
            """)
    enquire()


def enquire():
    print(""" 
    Would you like to perform another transaction? 
    
    1-> Back to Main Menu
    2-> Exit
    """)
    response = int(input("enter a number: "))
    if response == 1:
        display()
    elif response == 2:
        print(f"""
        #############@@@@@@@@@@@@@@@@@@@@############
            Thank you for choosing Shebotimo Bank
        #############@@@@@@@@@@@@@@@@@@@@############
        """)
        exit()

    else:
        print("invalid input")


def deposit_cash():
    receivers_account_num = int(input("kindly enter your account number: "))
    receivers_name = input("Kindly enter your name: ")
    amount = int(input("Enter your amount: "))
    bank.deposited(amount, receivers_account_num)
    print(
        f"""
    ************************************************
        Hello {receivers_name}
        Your account number {receivers_account_num}
        Has been credited with {amount}
    ************************************************
    
    """
    )
    enquire()


def withdraw_cash():
    global pin
    recipients_account_number = int(input("kindly enter your account number: "))
    amount = int(input("Kindly enter amount:"))
    pin = int(input("Kindly input your pin: "))
    bank.to_withdraw(recipients_account_number, amount, pin)
    print(f"""
    ***************************************************************************
    Dear Customer, {amount} has been debited from your {recipients_account_number}, with us
    Thank you for banking with us!
    ***************************************************************************
    """)
    enquire()


def check_balance():
    global pin
    account_number = int(input("Kindly enter your account number: "))
    pin = input("Kindly input your pin: ")
    balance = bank.check_balance(account_number, pin)
    print(f"""
    Dear customer your balance is {balance}
    """)
    enquire()


if __name__ == '__main__':
    bank = Bank("Shebotimo Bank", "pin")
    welcome()
