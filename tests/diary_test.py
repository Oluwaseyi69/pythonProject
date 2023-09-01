import unittest

from LearnPyTest.Diary import Diary



class TestDiary(unittest.TestCase):
    def setUp(self) -> None:
        self.diary = Diary("Seyi", "1234")

    def test_that_diary_exist(self):
        self.assertIsNotNone(self.diary)

    def test_that_diary_is_locked(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())

    def test_that_diary_can_be_unlocked(self):
        self.diary.unlocked_diary("1234")
        self.assertFalse(self.diary.lock_diary())

    def test_that_diary_can_be_created(self):
        self.diary.create_new_entry(1,"My thoughts", "My thoughts are with me")
        self.assertEquals("1 My thoughts My thoughts are with me",self.diary.find_entry_by_id(1).get_entry())



if __name__ == '__main__':
    unittest.main()