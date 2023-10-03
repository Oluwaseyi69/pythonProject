import unittest

from LearnPyTest.tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def setUp(self) -> None:
        self.board = TicTacToe()

    def test_board_exist(self):
        self.assertTrue(self.board)

    def test_that_board_is_empty(self):
        self.board.board_is_empty()
        self.assertFalse(self.board.board_is_empty())

    def test_to_get_symbol(self):
        self.board.input_symbol("9 ")
        self.assertFalse(self.board.input_symbol("1"), "X")


if __name__ == '__main__':
    unittest.main()
