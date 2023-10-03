class TicTacToe:
    def __init__(self):
        self.board = [
            [' ', '|', ' ', '|', ' '],
            ['-', '+', '-', '+', '-'],
            [' ', '|', ' ', '|', ' '],
            ['-', '+', '-', '+', '-'],
            [' ', '|', ' ', '|', ' ']
        ]

    def board_is_empty(self):
        self.board = []
        if not self.board:
            print("board is empty")

    def input_symbol(self, value):
        if value == '1':
            self.board[0][0] = 'X'
        elif value == '2':
            self.board[0][2] = 'X'
        elif value == '3':
            self.board[0][4] = 'X'
        elif value == '4':
            self.board[2][0] = 'X'
        elif value == '5':
            self.board[2][2] = 'X'
        elif value == '6':
            self.board[2][4] = 'X'
        elif value == '7':
            self.board[4][0] = 'X'
        elif value == '8':
            self.board[4][2] = 'X'
        elif value == '9':
            self.board[4][4] = 'X'

        else:
            exit()

