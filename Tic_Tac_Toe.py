from IPython.display import clear_output

def display_board(board):
    clear_output()
    print("----- ----- -----")
    print('  '+board[7]+'  |'+'  '+board[8]+'  |'+'  '+board[9])
    print("----- ----- -----")
    print('  '+board[4]+'  |'+'  '+board[5]+'  |'+'  '+board[6])
    print("----- ----- -----")
    print('  '+board[1]+'  |'+'  '+board[2]+'  |'+'  '+board[3])
    print("----- ----- -----")

def player_input():

    marker = ''

    #KEEP ASKING PLAYER 1 to choose X or O

    while marker !='X' and marker !='O':
        marker=input('Player1, choose X or O: ').upper()

    #ASSIGN PLAYER 2, the opposite marker
    player1=marker
    if player1 == 'X':
        player2='O'
    else:
        player2 ='X'
    return(player1,player2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    # WIN TIC TAC TOE?
    #ALL ROWS, and check to see if they share the same marker
    return ((board[1]==mark and board[2]==mark and board[3]==mark)
    or (board[4]==mark and board[5]==mark and board[6]==mark)
    or (board[7]==mark and board[8]==mark and board[9]==mark)
    or (board[1]==mark and board[4]==mark and board[7]==mark)
    or (board[2]==mark and board[5]==mark and board[8]==mark)
    or (board[3]==mark and board[6]==mark and board[9]==mark)
    or (board[3]==mark and board[5]==mark and board[7]==mark)
    or (board[1]==mark and board[5]==mark and board[9]==mark))

    #ALL COLUMNS, and check to see if they share the same marker
    #DIAGONALS, and check to see if they share the same marker
    #USE INDEXING TO GRAB THEM!

import random
def choose_first():
    flip=random.randint(0,1)
    if flip ==0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    return board[position] == ''

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
        #BOARD IS FULL IF WE RETURN TRUE
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose a position:(1-9)'))
    return position

def replay():
    choice = input("Play again? Enter Yes or No")
    return choice == 'Yes'
# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to Tic Tac Toe')
while True:

    #PLAY THE GAME

    #SET EVERYTHING UP(BOARD, WHO IS FIRST, CHOOSE MARKERS

    the_board = ['']*10
    player1_marker,player2_marker=player_input()

    turn = choose_first()
    print(turn+' will go first')

    play_game = input('Ready to play? y or n')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    #GAME PLAY
    while game_on:

        if turn == 'Player 1':

        #Show the board
            display_board(the_board)
        #Choose a position
            position = player_choice(the_board)
        #Place the marker on the position
            place_marker(the_board,player1_marker,position)

        #Check if they won
        if win_check(the_board,player1_marker):
            display_board(the_board)
            print('PLAYER 1 HAS WON!')
            game_on=False
        ##else:
            if full_board_check(the_board):
                display_board(the_board)
                print('TIE!')
                game_on=False
            else:
                turn = 'Player 2'
        #Or check if there is a tie

    #PLAYER ONE TURN

    #No tie, no win, next player's turn
        else:
        #Show the board
             display_board(the_board)
        #Choose a position
        position = player_choice(the_board)
        #Place the marker on the position
        place_marker(the_board,player2_marker,position)

        #Check if they won
        if win_check(the_board,player2_marker):
            display_board(the_board)
            print('PLAYER 2 HAS WON!')
            game_on=False
        else:
            if full_board_check(the_board):
                display_board(the_board)
                print('TIE!')
                game_on=False
            else:
                turn = 'Player 1'


    #PLAYER TWO TURN


    if not replay():
        break
#BREAK OUT OF THE WHILE LOOP ON THE REPLAY FUNCTION
