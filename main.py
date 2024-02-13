def board(board):
    return board[0] + ' | ' + board[1] + ' | ' + board[2] + '\n----------\n' + board[3] + ' | ' + board[4] + ' | ' + board[5] + '\n----------\n' + board[6] + ' | ' + board[7] + ' | ' + board[8]

def position_choice():
    '''
    In choice variable there are restrictions and returns
    the integer of the position of the list
    '''
    choice = 'Wrong'
    while choice not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
        choice = input('Enter position (0-8): ')
        if choice not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
            print('Invalid input.')
    return int(choice)

def user_replacement(board, pos, symbol):
    board[pos] = symbol
    return board

if __name__ == '__main__':
    game_list = board([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    print('Welcome to Tic Tac Toe!')
    print('Here is the current board.')
    print(game_list)


    first_player_symbol = 'NULL'
    while first_player_symbol not in ['X', 'O']:
        first_player_symbol = input('Enter your symbol (first player): ')
        if first_player_symbol not in ['X', 'O']:
            print('Invalid input.')
    pos1 = position_choice()
    game_list = user_replacement(game_list, pos1, first_player_symbol)

    second_player_symbol = 'X' if first_player_symbol == 'O' else 'O'

    print(board(game_list))

