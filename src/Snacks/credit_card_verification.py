import struct


card_number = ""

def card_length():
    global card_number
    try:
        card_number_entered = int(input("Enter card number: "))
        print("**Credit Card Number: ", card_number_entered)

        card_number = str(card_number_entered)

        if len(card_number) >= 13 or len(card_number) <= 16:
            print("**Credit Card Length:", len(card_number))
            card_type()
        else:
            card_length()
    except (ValueError, KeyboardInterrupt, SyntaxError, TypeError, ZeroDivisionError, RecursionError):
        print("Invalid Input, Try Again")
        card_length()



def card_type():
    try:
        if card_number.startswith("4"):
            print('**Credit Card Type: Visa cards')
            card_validity()
        elif card_number.startswith("5"):
            print("**Credit Card Type: Master card")
            card_validity()
        elif card_number.startswith("37"):
            print('**Credit Card Type: American Express Cards')
            card_validity()
        elif card_number.startswith("6"):
            print("**Credit Card Type: Discover cards")
            card_validity()
        else:
            card_type()
    except (ValueError, KeyboardInterrupt, SyntaxError, TypeError, ZeroDivisionError, RecursionError):
        # print("Enter a valid number")
        card_type()


def card_validity():

    try:
        total = 0
        alternate = False
        for digit in card_number[:: -1]:
            digit = int(digit)
            if alternate:
                digit *= 2
                if digit >9:
                    digit-=9
            total+=digit
            alternate = not alternate

        if total % 10 == 0:
            print("**Credit card Validity Status: Valid")
        else:
            print("**Credit card Validity Status: invalid")
    except (ValueError, KeyboardInterrupt, SyntaxError, TypeError, ZeroDivisionError):
        card_validity()


card_length()