import random

player_positions = []
computer_positions = []


def print_board(board):
    for row in board:
        for char in row:
            print(char, end='')
        print()


def piece(board, position, user):
    symbol = ' '
    if user == "player":
        symbol = 'X'
        player_positions.append(position)
    elif user == "computer":
        symbol = 'O'
        computer_positions.append(position)

    if position == 1:
        board[0][0] = symbol
    elif position == 2:
        board[0][2] = symbol
    elif position == 3:
        board[0][4] = symbol
    elif position == 4:
        board[2][0] = symbol
    elif position == 5:
        board[2][2] = symbol
    elif position == 6:
        board[2][4] = symbol
    elif position == 7:
        board[4][0] = symbol
    elif position == 8:
        board[4][2] = symbol
    elif position == 9:
        board[4][4] = symbol


def check_winner(player_positions, computer_positions):
    # global computer_positions
    # global player_positions

    win = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [7, 5, 3]
    ]

    for winner in win:
        if all(position in player_positions for position in winner):
            return "Congratulations you won!!!"
        elif all(position in computer_positions for position in winner):
            return "Computer Wins!!!"
        elif len(player_positions) + len(computer_positions) == 9:
            return "It's a Draw"

    return ""


def welcome():
    print(f"""
        *******************
        TIC-TAC-TOE
        *******************
    
        In this game you'd get to play with computer
        and you have one print board on the screen 
        where there are boxes of 1-9 that can be filled with either X or O 
        which can be used to mark their cells
        Enjoy!!!
    """)


def option():
    print(f"""
       1-> Play game
       2-> Exit      
    """)
    try:
        user_input = int(input("Enter a number: "))
        if user_input == 1:
            main()
        elif user_input == 2:
            print("Thank you for playing")
            exit()
        else:
            print("Enter a valid option.")
            option()
    except(ValueError, TypeError, NameError, KeyError, KeyboardInterrupt, ZeroDivisionError):
        print("Kindly Input correct Information")
        option()


def main():
    board = [
        [' ', '|', ' ', '|', ' '],
        ['-', '+', '-', '+', '-'],
        [' ', '|', ' ', '|', ' '],
        ['-', '+', '-', '+', '-'],
        [' ', '|', ' ', '|', ' ']
    ]

    print_board(board)

    while True:
        print("Enter your number between 1-9: ")

        player_position = int(input())
        while player_position in player_positions or player_position in computer_positions:
            print("Position taken! Enter a correct position: ")
            player_position = int(input())

        piece(board, player_position, "player")
        if result := check_winner(player_positions, computer_positions):
            print(result)
            break

        computer_position = random.randint(1, 9)
        while computer_position in player_positions or computer_position in computer_positions:
            computer_position = random.randint(1, 9)

        piece(board, computer_position, "computer")
        print_board(board)
        if result := check_winner(player_positions, computer_positions):
            print(result)
            break


if __name__ == "__main__":
    welcome()
    option()
