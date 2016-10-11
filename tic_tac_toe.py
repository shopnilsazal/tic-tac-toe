# Global Variables
board = [' '] * 10
game_state = True
announce = ''


def reset_board():
    global board, game_state
    board = [' '] * 10
    game_state = True


def display_board():
    """ This function prints out the board so the numpad can be used as a reference """
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('-' * 11)
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('-' * 11)
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')


def win_check(board, player):
    if (board[7] == board[8] == board[9] == player) or (board[4] == board[5] == board[6] == player) or \
            (board[1] == board[2] == board[3] == player) or (board[7] == board[4] == board[1] == player) or \
            (board[8] == board[5] == board[2] == player) or (board[9] == board[6] == board[3] == player) or \
            (board[7] == board[5] == board[3] == player) or (board[9] == board[5] == board[1] == player):
        return True
    else:
        return False


def full_board_check(board):
    """ Function to check if any remaining blanks are in the board """
    if ' ' in board[1:]:
        return False
    else:
        return True


def choose_mark():
    mark = input('What you want to choose? (X/O) ')
    if mark.upper() == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def ask_player(mark):
    """ Asks player where to place X or O mark, checks validity """
    global board
    req = 'Choose where to place your: ' + mark + ' '
    while True:
        try:
            choice = int(input(req))
        except ValueError:
            print('Sorry, Please enter a number between 1-9.')
            continue

        if board[choice] == ' ':
            board[choice] = mark
            break
        else:
            print('That space is not empty!')
            continue


def player_choice(mark):
    global board, game_state, announce
    # Set game announcement blank
    announce = ''
    mark = str(mark)
    ask_player(mark)

    if win_check(board, mark):
        display_board()
        announce = mark + ' wins! Congratulations.'
        game_state = False

    display_board()

    if full_board_check(board):
        announce = 'Tie!'
        game_state = False

    return game_state, announce


def play_game():
    reset_board()
    global announce

    p1, p2 = choose_mark()

    while True:
        # Player 1 turn
        game_state, announce = player_choice(p1)
        print(announce)
        if not game_state:
            break

        # Player 2 turn
        game_state, announce = player_choice(p2)
        print(announce)
        if not game_state:
            break

    # Ask for rematch
    rematch = input('Would you like to play again? (y/n) ')
    if rematch == 'y':
        play_game()
    else:
        print('Thanks for playing!')

play_game()
