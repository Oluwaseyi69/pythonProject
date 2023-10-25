import random
from LearnPyTest.account import *



class Bank:
    def __init__(self, bank_name, pin):
        self.bank_name = bank_name
        self.pin = pin
        self.__list_of_accounts = []
        self.validate_account_number

    def register(self, firstName, lastName, pin):
        format_name = f"{firstName} {lastName}"
        account = Account(self.__generate_account_number(), format_name, pin)
        self.__list_of_accounts.append(account)
        return account

    def find_account(self, account_number):
        
        for account in self.__list_of_accounts:
            if account.get_account() != account_number:
                return ValueError("Account Not Found")
            if account:

                return account

    def deposited(self, amount, account_number):
        return self.find_account(account_number).deposit(amount)

    def check_balance(self, account_number, pin):
        return self.find_account(account_number).getBalance(pin)

    def to_withdraw(self, account_number, amount, pin):
        return self.find_account(account_number).withdraw(amount, pin)

    def __generate_account_number(self):
        return len(self.__list_of_accounts) + 1

    def list_of_account(self):
        return "the number of account is: ", len(self.__list_of_accounts)
        #  account_num = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        #             return account_num

    # def transfer(self, sender_account_number, receiver_account_number, amount, pin ):
    #     self.find_account(sender_account_number).withdraw(amount, pin)
    #     self.find_account(receiver_account_number).deposit(amount)
