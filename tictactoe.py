import random

test_board = ['#', 'X', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'O']

def display_rules():

    # This fountion is to guide the player about the game
    print('Here are the rules of the game: ')
    print('Select the position of your marker ("X" or "O") from the numpad\nfrom 1 to 9. The layout of the the positions is shown below')
    print('-----------------------------------------------------------------')
    print('7 ' + '| ' + '8 ' + '| ' + '9 ')
    print('- ' + '- ' + '- ' + '- ' + '- ')
    print('4 ' + '| ' + '5 ' + '| ' + '6 ')
    print('- ' + '- ' + '- ' + '- ' + '- ')
    print('1 ' + '| ' + '2 ' + '| ' + '3 ')
    print('-----------------------------------------------------------------')
    print('You can select "Y" or "N" for "Yes" or "No" when asked')

def display_board(board):

    # Showing the empty layoyt of the board!
    print("\n"*50)
    print(board[9] + ' | ' + board[8] + ' | ' + board[9])
    print('- ' + '- ' + '- ' + '- ' + '- ')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('- ' + '- ' + '- ' + '- ' + '- ')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print("\n")


def player_input():

    # This function is to ask the choice of weapon 'X' or 'O'

    choice = '' # Taking the choice of player_1

    while choice != 'X' and choice != 'O':

        choice = input("Player 1 please select your choice of weapon ('X' or 'O'): ").upper()

    if choice != 'X' and choice != 'O':
        print('Please choose the mentioned weapons')

    player_1 = choice

    if choice == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'

    return(player_1, player_2) # Returning the final choice of the players!

def place_marker(board, marker, position):

    board[position] = marker

def win_check(board, marker):

    return((board[1] == board[2] == board[3] == marker) or
    (board[4] == board[5] == board[6] == marker) or
    (board[7] == board[8] == board[9] == marker) or
    (board[1] == board[4] == board[7] == marker) or
    (board[2] == board[5] == board[8] == marker) or
    (board[3] == board[6] == board[9] == marker) or
    (board[7] == board[5] == board[3] == marker) or
    (board[1] == board[5] == board[9] == marker))

def choose_first():

    flip = random.randint(1, 2)

    if flip == 1:
        return 'Player 1'
    else:
        return "Player 2"

def space_check(board, position):

    return board[position] == ' '

def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Choose a position: (1-9): "))
    
    return position

def replay():

    choice = input("Play again? Enter Y or N: ").upper()

    return choice == 'Y'

print("Welcome to Tic Tac Toe!")
display_rules()

while True:

    the_board = [' ']*10
    player_1_marker , player_2_marker = player_input()

    turn = choose_first()

    print(turn + ' will go first')

    play_game = input('Ready to play? Y or N: ').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    
    while game_on:

        if turn == 'Player 1':

            # Player 1 turn

            # Show the board
            display_board(the_board)

            # Choose a position
            position = player_choice(the_board)

            # Place the marker on the position
            place_marker(the_board, player_1_marker, position)

            #Check if they won?
            if win_check(the_board, player_1_marker):
                display_board(the_board)
                print('Player 1 has WON!!')
                game_on = False
            else:                                   # Check for a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game ends in a TIE!!")
                    game_on = False

                else:
                    turn = "Player 2"  # if no tie then player 2 turn
        else:

            # Player 2 turn

            # Show the board
            display_board(the_board)

            # Choose a position
            position = player_choice(the_board)

            # Place the marker on the position
            place_marker(the_board, player_2_marker, position)

            #Check if they won?
            if win_check(the_board, player_2_marker):
                display_board(the_board)
                print('Player 2 has WON!!')
                game_on = False
            else:                                   # Check for a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game ends in a TIE!!")
                    game_on = False
                else:
                    turn = "Player 1"  # if no tie then player 1 turn

    if not replay():
        break
    # Break out of the WHILE loop on replay()

