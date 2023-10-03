import unittest

from tic_tac_toe.tic_tac_toe import *

player_positions = []
computer_positions = []


class TestTicTacToe(unittest.TestCase):

    def test_print_board(self):
        board = [
            [' ', '|', ' ', '|', ' '],
            ['-', '+', '-', '+', '-'],
            [' ', '|', ' ', '|', ' '],
            ['-', '+', '-', '+', '-'],
            [' ', '|', ' ', '|', ' ']
        ]
        expected_output = [
            [' ', '|', ' ', '|', ' '],
            ['-', '+', '-', '+', '-'],
            [' ', '|', ' ', '|', ' '],
            ['-', '+', '-', '+', '-'],
            [' ', '|', ' ', '|', ' ']
        ]
        self.assertEqual(board, expected_output)

    def test_piece(self):
        board = [
            ['X', '|', 'O', '|', ' '],
            ['-', '+', '-', '+', '-'],
            [' ', '|', 'X', '|', ' '],
            ['-', '+', '-', '+', '-'],
            ['O', '|', ' ', '|', ' ']
        ]
        piece(board, 9, "player")
        expected_board = [
            ['X', '|', 'O', '|', ' '],
            ['-', '+', '-', '+', '-'],
            [' ', '|', 'X', '|', ' '],
            ['-', '+', '-', '+', '-'],
            ['O', '|', ' ', '|', 'X']
        ]
        self.assertEqual(board, expected_board)

    def test_check_winner_player_wins(self):
        player_positions = [1, 2, 3]
        computer_positions = [4, 5, 6]
        result = check_winner(player_positions, computer_positions)
        self.assertEqual(result, "Congratulations you won!!!")

    def test_check_winner_computer_wins(self):
        computer_positions = [2, 5, 8]
        player_positions = [1, 4, 7]
        result = check_winner(computer_positions, player_positions)
        self.assertEqual(result, "Computer Wins!!!")

    def test_check_winner_draw(self):
        player_positions = [1, 2, 4, 5]
        computer_positions = [3, 6, 7, 8, 9]
        result = check_winner(player_positions, computer_positions)
        self.assertEqual(result, "It's a Draw")


if __name__ == '__main__':
    unittest.main()
