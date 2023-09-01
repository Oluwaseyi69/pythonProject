import unittest

from LearnPyTest.account import Account



def validate_pin():
    pass


class TestAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.account = Account("1","seyi","temitope")
    def test_that_account_exist(self):
        self.assertIsNotNone(self.account)

    def test_that_amount_can_be_deposited(self):
        self.account.deposit(2000)
        self.assertEquals(2000,self.account. getBalance("temitope"))

    def test_that_money_withdrawal(self):
        self.account.deposit(2000)
        self.account.withdraw(500)

        self.assertEquals(self.account.getBalance("temitope"), 1500)
        self.account.deposit(3000)
        self.account.update_pin("temitope","temtope")
        self.assertEquals(4500,self.account.getBalance("temtope"))


    def test_to_check_to_update_pin(self):
        self.account = Account("2","seyi", "temitope")
        validate_pin()
        self.assertEquals(self.account.validate_pin(), "temitope")




    # def deposit(self, param, param1):
    #     pass

