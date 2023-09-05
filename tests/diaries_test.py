import unittest

from LearnPyTest import Diaries


from LearnPyTest.Diaries import Diaries


class TestDiaries(unittest.TestCase):
    def setUp(self) -> None:
        self.diaries = Diaries()

    def test_that_diary_can_added(self):
        self.diaries.add_diary("seyi", "password")
        self.assertTrue("seyi password",
                          self.diaries.find_by_username("seyi"))

    def test_that_diary_can_be_deleted(self):
        self.diaries.delete_diary("seyi", "password")
        self.assertTrue("seyi password",self.diaries.find_by_username("seyi"))