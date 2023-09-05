import unittest

from LearnPyTest.Diary import Diary



class TestDiary(unittest.TestCase):
    def setUp(self) -> None:
        self.diary = Diary("Seyi", "1234")

    def test_that_diary_exist(self):
        self.assertIsNotNone(self.diary)

    def test_that_diary_is_locked(self):
        self.diary.is_locked()
        self.assertTrue(self.diary.is_locked())

    def test_that_diary_can_be_unlocked(self):
        self.diary.unlocked_diary("1234")
        self.assertTrue(self.diary.is_locked())

    def test_that_diary_can_be_created(self):
        self.diary.create_new_entry(1,"My thoughts", "My thoughts are with me")
        self.assertEquals("1 My thoughts My thoughts are with me",self.diary.find_entry_by_id(1).get_entry())

    def test_that_diary_can_be_found(self):
        self.diary.create_new_entry(1, "My thoughts", "My thoughts are with God")
        self.diary.find_entry_by_id(1)
        self.assertTrue("1 My thoughts, My thoughts are with God")

    def test_that_entry_can_be_deleted(self):
        self.diary.create_new_entry(1, "My thoughts", "My thoughts are with God")
        self.assertEquals("1 My thoughts My thoughts are with God",self.diary.find_entry_by_id(1).get_entry())
        self.diary.delete_entry(1)
        self.assertRaises(ValueError,self.diary.find_entry_by_id, 1)

if __name__ == '__main__':
    unittest.main()