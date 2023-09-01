import unittest
from test.television import Television

class TestTelevision(unittest.TestCase):
    def test_tv_is_on(self):
        self.tv = Television()
        self.tv.turn_on()
        self.assertTrue(self.tv.isOn)

    def test_tv_is_off(self):
        self.tv = Television()
        self.tv.turn_off()
        self.assertFalse(self.tv.isOn)

    def test_that_television_can_set_channel(self):
        self.tv = Television()
        self.tv.turn_on()
        self.assertTrue(self.tv.isOn)

        self.tv.set_channel(9)
        self.assertEqual(self.tv.get_channel(), 9)

    def test_that_television_can_set_channel_up(self):
        self.tv = Television()
        self.tv.turn_on()

        self.tv.set_channel(10)
        self.tv.channel_up()
        self.assertEqual(self.tv.get_channel(), 11)

    def test_that_television_can_make_volume_up(self):
        self.tv = Television()
        self.tv.turn_on()

        self.tv.set_volume(10)
        self.tv.volume_up()
        self.assertEqual(self.tv.get_volume(), 11)

    def test_that_television_can_make_volume_down(self):
        self.tv = Television()
        self.tv.turn_on()

        self.tv.set_volume(10)
        self.tv.volume_down()
        self.assertEqual(self.tv.get_volume(), 9)




unittest.main()