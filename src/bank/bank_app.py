




















































# class Bank:
#     def __init__(self, account_number,account_name,balance = 0.0):
#         self.account_number = account_number
#         self.account_name = account_name
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return True
#         else:
#             return False
#
#
#     def withdraw(self, amount):
#         if amount > 0 or amount < self.balance:
#             self.balance -= amount
#             return True
#         else:
#             return False
#
#     def get_balance(self):
#         return self.balance
#
# class BankApp:
#     def __init__(self):
#         self.accounts = {}
#
#     def new_accounts(self, account_number, account_name):
#         if account_number not in self.accounts:
#             self.accounts[account_number] = Bank(account_number, account_name)
#             print("New account created")
#         else:
#             print("Account already exists.")
#
#     def check_account(self, account_number):
#         if account_number in self.accounts:
#             return self.accounts[account_number]
#
#
# def main():
#     bank_app = BankApp
#
#     try:
#
#         while True:
#             print("\n Welcome to Six9ine Bank Account App")
#             print("1. Create Account")
#             print("2. Access Account")
#             print("3. Exit")
#             user_input = input("Enter a number: ")
#
#             if user_input == "1":
#                 account_number = input("Enter Account Number: ")
#                 account_name =input("Enter Account Name: ")
#                 bank_app.new_accounts(account_number,account_name)
#
#                 # main()
#
#             elif user_input == "2":
#                 account_number = input("Enter Account Number: ")
#                 account = bank_app.check_account(BankApp,account_number)
#                 if account == bank_app.check_account(BankApp,account_number):
#
#                     # while True:
#                         print(""" \nAccount Menu
#                                 1. Deposit
#                                 2. Withdraw
#                                 3. Check Balance
#                         """)
#                         user_input =input("Enter a number: ")
#
#                         if user_input == "1":
#                             amount =float(input("Enter amount to be deposited: "))
#                             account.deposit(amount)
#                             print("Amount Successfully deposited")
#                         elif user_input == "2":
#                             amount = float(input("Enter amount: "))
#                             if account.withdraw(amount):
#                                 print("Successful")
#                             else:
#                                 print("Invalid transaction")
#                         elif user_input == "3":
#                             print("Balance"+ account.get_balance())
#
#                         else:
#                             print("invalid option")
#                 else:
#                     print("invalid")
#             else:
#                 print("Exit")
#
#
#     except (NameError, ValueError, AttributeError,TypeError):
#         main()
#
#
# if __name__ == "__main__":
#     main()
#
#
#
#
#
#
