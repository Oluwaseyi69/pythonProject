from tests.account_test import validate_pin
from account import *


class Account:
    balance = 0
    accountNumber = None
    accountName = None
    pin = None

    def __init__(self, accountNumber, accountName, pin):
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.pin = pin

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("deposit a valid amount")
        elif amount > 0:
            self.balance += amount
        return self.balance


    def getBalance(self,pin):
        if self.pin == pin:
            return self.balance
        else:
            raise ValueError("deposit a valid amount")


    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Withdrawal impossible, Enter a valid amount")

        else:
            self.balance -= amount
        return self.balance

    def withdraw_less(self, amount):
        if self.balance > amount:
            raise ValueError("impossible")
        else:
            self.balance -= amount
            return self.balance

    def update_pin(self, oldPin,newPin):
        if self.pin == oldPin:
            self.pin = newPin
            return newPin

        else:
            raise TypeError ("Enter a different pin")

    def validate_pin(self):
        if self.pin != self.pin:
            raise ValueError("Enter the correct pin")
        else:
            return self.pin

    def get_account(self) -> str:
        return self.accountName

    def get_account_name(self):
        return self.accountName

    def get_account_number(self):
        return self.accountNumber