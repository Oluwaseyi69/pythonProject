import unittest
import tests as test

from LearnPyTest.bank import Bank



class TestBank(unittest.TestCase):
    def setUp(self) :
        self.bank = Bank("UBA")

    def testThatBankCanRegisterAccount(self):
        bank = Bank("First Bank")
        acct = bank.register("Seyi", "Banwo","1234")
        print(acct.accountNumber)
        self.assertIsNotNone(acct)

    def test_to_deposit_money(self):
        self.bank.register("Seyi", "Banwo", "1234")
        self.bank.deposited(3000, "1")
        self.assertEqual("Seyi Banwo", self.bank.find_account("1").get_account())
        self.assertEquals(3000,self.bank.check_balance("1", "1234"))

    def test_to_be_able_to_withdraw(self):
        self.bank.register("Seyi", "Banwo", "1234")
        self.bank.deposited(4000, "1")
        self.assertEqual("Seyi Banwo", self.bank.find_account("1").get_account())
        self.assertEquals(self.bank.check_balance("1", "1234"), 4000)
        self.bank.to_withdraw("1",3000, "1234")
        self.assertEquals(self.bank.check_balance("1", "1234"), 1000)

    # def test_that_i_cant_withdraw_above_balance(self):
    #     self.bank = Bank()
    #     self.bank.register("Seyi", "Banwo", "1234")
    #     self.bank.deposited(4000, "1")
    #     self.assertEqual("Seyi Banwo", self.bank.find_account("1").get_account())
    #     self.assertEquals(self.bank.check_balance("1", "1234"), 4000)
    #     # self.bank.to_withdraw("1", 5000, "1234")
    #     self.assertRaises(ValueError, self.bank.to_withdraw, 5000, "1", "1234" )
    #     self.assertEqual(self.bank.check_balance("1","1234"),4000)






        





