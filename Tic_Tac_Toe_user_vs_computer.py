"""
@Author: Umer Shahzad
Created on: 26/07/2023
"""


import random


def print_board(board):
    """Function to display the board"""
    i, j, k = 0, 1, 2
    print("\t\t<< TIC TAC TOE >>")

    for x in range(3):

        print("\t\t  -------------")
        print("\t\t  | " + str(board[i]) + " | " + str(board[j]) + " | " + str(board[k]) + " | \t\t ")
        i, j, k = i+3, j+3, k+3

    print("\t\t  -------------")

    """This method is for checking the winner 
    @:param board: which represents a list of points which we select for turn
    @:param player :which represents the user who's playing against computer """


def check_win(board, player):
    """Function to check all the winning conditions"""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows Conditions
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns Conditions
        [0, 4, 8], [2, 4, 6]  # Diagonals Conditions
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True

    return False

    """This method is for checking the empty spots in board list for user turn
    @:param board: which represents a list of points which we select for turn
    """


def get_empty_spots(board):
    """Function to get a list of empty spots on the board using list comprehension"""
    return [i for i in range(len(board)) if board[i] != "X" and board[i] != "$"]

    """This method is working as a main function which handles all the function calls and inputs"""


def tic_tac_toe():
    """Function to play tic-tac-toe against the computer"""

    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player = "X"


    while True:
        """Loop for running the turns of players and computer"""
        print_board(board)
        #
        try:
            if player == "X":
                print("Player X turn.")
                move = int(input("Enter a number from 0-8: "))

                while move >=9 or move < 0:
                  move = int(input("Enter a number from 0-8: "))
            else:
                """Computer's turn (select a random move from the available empty spots)"""
                possible_moves = get_empty_spots(board)
                move = random.choice(possible_moves)

            if board[move] != "X" and board[move] != "$":
                board[move] = player

                if check_win(board, player):
                    print_board(board)
                    print(f"Congratulations! Player {player} wins!")
                    break

               # Switch player for the next turn
                player = "X" if player == "$" else "$"

            else:
             print("That spot is already taken! Try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except IndexError:
            print("Invalid move. Please enter a number from 0 to 8.")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Check if the board is full (tie situation)
        if len(get_empty_spots(board)) == 0:
            print_board(board)
            print("It's a tie!")
            break


tic_tac_toe()
n = input("you wanna play again (yes/no) :").lower()

"""This while loop will work only if user enter 'yes' for playing again """
while True:
    if n == "yes":
        tic_tac_toe()
        n = input("you wanna play again (yes/no) :").lower()

    else:
        break

