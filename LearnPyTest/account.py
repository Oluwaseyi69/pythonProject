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

    def getBalance(self, pin):
        self.validate_pin(pin)
        return self.balance
        # else:
        #     raise ValueError("deposit a valid amount")

    def withdraw(self, amount, pin):
        self.validate_pin(pin)
        if self.balance < amount:
            raise ValueError("Insufficient Fund")
        else:
            self.balance -= amount
        return self.balance

    def validate_pin(self, pin):
        if self.pin != pin:
            raise ValueError("Enter the correct pin")

    def update_pin(self, oldPin, newPin):
        self.validate_pin(oldPin)
        self.pin = newPin
        return newPin

    def get_account(self) -> str:
        return self.accountName

    def get_account_name(self):
        return self.accountName

    def get_account_number(self):
        return self.accountNumber
