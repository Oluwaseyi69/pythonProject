import unittest

from menstrual.notification import Notification
from menstrual.user_class import User


# from menstrualCycle.user import User, Notification

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User(1, "seyi", "email", "password")

    def test_user_can_be_added(self):
        self.user.add_user(1, "here is my flow")
        self.assertEqual(self.user.get_user_id(), Notification(1, "here is my flow").get_notification_id())

    def test_user_can_be_deleted(self):
        self.user.add_user(1, "the flow is much!!!")
        self.user.delete_user(1)
        with self.assertRaises(ValueError):
            self.user.find_user(1)

    def test_user_can_update_symptoms(self):
        self.user.add_user(1, "the flow is much!!!")
        self.user.update_user(1, "the flow has reduced thank you.")
        self.assertEqual(self.user.get_user_id(),
                         Notification(1, "the flow has reduced thank you.").get_notification_id())

    def test_cycle_length(self):
        self.user.add_user(1, "the flow is much!!!")
        actual = self.user.get_cycle_length(27, 31, 25, 3)
        expected = 27
        self.assertEqual(actual, expected)

    def test_ovulation_period(self):
        self.user.add_user(1, "the flow is much!!!")
        actual = self.user.ovulation_period(28)
        expected = 12
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
