import unittest

from LearnPyTest.check_isogram import Isogram


class TestIsogram(unittest.TestCase):
    def setUp(self):
        self.isogram = Isogram("word")

    def testToCheckAlphabet(self):
        self.isogram.check_isogram("d1wer ftgyu")
        self.assertTrue(self.isogram.check_isogram("d1wer ftgyu"))
