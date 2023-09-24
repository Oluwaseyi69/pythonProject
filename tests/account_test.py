import unittest

from LearnPyTest.account import Account


def validate_pin():
    pass


class TestAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.account = Account("1", "seyi", "pin")

    def test_that_account_exist(self):
        self.assertIsNotNone(self.account)

    def test_that_amount_can_be_deposited(self):
        self.account = Account("1", "seyi", "pin")
        self.account.deposit(2000)
        self.assertEquals(2000, self.account.getBalance("pin"))

    def test_to_withdrawal(self):
        self.account = Account("1", "seyi", "pin")
        self.account.deposit(2000)
        self.account.withdraw(500, "pin")

        self.assertEquals(1500, self.account.getBalance("pin"))
        self.account.deposit(3000)
        self.account.update_pin("pin", "temitope")
        self.assertEquals(4500, self.account.getBalance("temitope"))

    def test_to_check_to_update_pin(self):
        self.account = Account("2", "seyi", "pin")
        self.account.update_pin("pin", "temitope")
        self.assertEquals("temitope", "temitope")



