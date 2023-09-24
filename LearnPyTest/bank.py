import random
from LearnPyTest.account import Account


class Bank:
    def __init__(self, bank_name, pin):
        self.bank_name = bank_name
        self.pin = pin
        self.__list_of_accounts = []

    def register(self, firstName, lastName, pin):
        format_name = f"{firstName} {lastName}"
        account = Account(self.get_account_number(), format_name, pin)
        self.__list_of_accounts.append(account)
        return account

    # def __generate_account_number(self):
    #     # self.bank_name
    #     account_number = ''
    #     for account_number in range(10):
    #         number = random.randint(0, 9)
    #         str(account_number) + str(number)
    #     return account_number

    def find_account(self, account_number):
        for account in self.__list_of_accounts:
            if account.get_account_number() == account_number:
                return account

            else:
                return ValueError("Account Not Found")

    def deposited(self, amount, account_number):
        return self.find_account(account_number).deposit(amount)

    def check_balance(self, account_number, pin):
        return self.find_account(account_number).getBalance(pin)

    def to_withdraw(self, account_number, amount, pin):
        return self.find_account(account_number).withdraw(amount, pin)

    def get_account_number(self):
        return len(self.__list_of_accounts) + 1
