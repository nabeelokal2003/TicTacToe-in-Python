def board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


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

def is_winner(board, symbol):
    # Checking rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == symbol:
            return True

    # Checking columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == symbol:
            return True

    if board[0] == board[4] == board[8] == symbol:
        return True

    if board[2] == board[4] == board[6] == symbol:
        return True

    return False

if __name__ == '__main__':

    game_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    print('Welcome to Tic Tac Toe!')
    print('Here is the current board.')
    board(game_list)

    first_player_symbol = 'NULL'
    while first_player_symbol not in ['X', 'O']:
        first_player_symbol = input('Enter your symbol (first player): ').upper()
    if first_player_symbol not in ['X', 'O']:
        print('Invalid input.')

    second_player_symbol = 'X' if first_player_symbol == 'O' else 'O'

    while True:
        pos1 = position_choice()
        user_replacement(game_list, pos1, first_player_symbol)
        board(game_list)

        if is_winner(game_list, first_player_symbol):
            print('First player is the winner!')
            break
        if is_winner(game_list, second_player_symbol):
            print('Second player is the winner!')
            break

        pos2 = position_choice()
        user_replacement(game_list, pos2, second_player_symbol)
        board(game_list)

        if is_winner(game_list, first_player_symbol):
            print('First player is the winner!')
            break
        if is_winner(game_list, second_player_symbol):
            print('Second player is the winner!')
            break