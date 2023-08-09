import re


# def main():
card_number = input("Enter a number: ")

card_number = ''.join(filter(str.isdigit, card_number))
visa_card = r'^4\d{15}$'
master_card = r'^5[1-5]\d{14}$'
american_express = r'^3[47\d{13}$'
discover_card = r'^6\d{15}$'

if re.match(visa_card, card_number):
    print("**Credit card type: Visa")
elif re.match(master_card, card_number):
    print("**Credit card type: MasterCard")
elif re.match(american_express, card_number):
    print("**Credit card type: American Express Card")
elif re.match(discover_card, card_number):
    print("**Credit card type: Discover card")
card_number = ''.join(filter(str.isdigit, card_number))
print("**Credit card number: ", card_number)
if '13' >= card_number <= '16':
    print("**Credit Card Length:", len(card_number))
elif len(card_number) <13:
    print('nil')
elif len(card_number) > 16:
    print("card number too long", len(card_number))
else:
    print("input a valid details: ")


is_double = False
total = 0
reversed_digits = card_number[::-1]
for y in reversed_digits:
    digit = int(y)
    if is_double:
        digit *= 2
        if digit > 9:
            digit -= 9
    total += digit
    is_double = not is_double

if total % 10 == 0:
    print("**Credit card Validity Status: Valid")
else:
    print("**Credit card Validity Status: Invalid")
