import os

game = True
player = True
board = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'}
count = 0

clear = lambda: os.system('cls')

def board_printer(b):
        print('  {}  |  {}  |  {}  '.format(b['1'],b['2'],b['3']))
        print('--------------------')
        print('  {}  |  {}  |  {}  '.format(b['4'],b['5'],b['6']))
        print('--------------------')
        print('  {}  |  {}  |  {}  '.format(b['7'],b['8'],b['9']))

def player_one(b,turn):
    chc = True
    print('Player one turn')
    move = input('Where do you whant to put X\n')
    while chc:
        if b[move] == '':
            b[move] = 'X'
            turn = False
            break
        elif b[move] != '':
            print('It is taken !!')
            input('Try one more time')
            continue
    return b,turn

def player_two(b,turn):
    print('Player two turn')
    move = input('Where do you whant to put O\n')
    if b[move] == '':
        b[move] = 'O'
        turn = True
    elif b[move] != '':
        print('It is taken !!')
    return b,turn

def check(b):
    if b['1'] == b['2'] and b['2'] == b['3'] and b['1'] !='':
        return True
    elif b['4'] == b['5'] and b['5'] == b['6'] and b['4'] !='':
        return True
    elif b['7'] == b['8'] and b['8'] == b['9'] and b['7'] !='':
        return True
    elif b['1'] == b['4'] and b['4'] == b['7'] and b['1'] !='':
        return True
    elif b['2'] == b['5'] and b['5'] == b['8'] and b['2'] !='':
        return True
    elif b['3'] == b['6'] and b['6'] == b['9'] and b['3'] !='':
        return True
    elif b['1'] == b['5'] and b['5'] == b['9'] and b['1'] !='':
        return True
    elif b['3'] == b['5'] and b['5'] == b['7'] and b['3'] !='':
        return True
    else:
        return False

print('Welcome !!\nIn TicTacToe game')
print('I will introduce you to this game, you have a board below:')
board_printer(board)
print('Remember the numbers in each squer because you will chose\nwhere do you whant to put your mark...')
print('" X " are starting good luck ;)')
input('Press any key to start ....')

board = {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}

while game == True:
    clear()
    win = check(board)

    if win:
        board_printer(board)
        if player:
            print('We got a winner!!!')
            print('The winner is O')
        else:
            print('We got a winner!!!')
            print('The winner is X')
        play = input('Do you what to play again?\nyes or no\n')
        if play == 'yes':
            board = {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}
            count = 0
            clear()
        else:
            break
    else:
        pass

    board_printer(board)
    if player == True:
        board,player = player_one(board,player)
    elif player == False:
        board,player = player_two(board,player)

    count += 1
    if count == 9:
        print('We got a draw !!!')
        play = input('Do you what to play again?\nyes or no\n')
        if play == 'yes':
            board = {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}
            count = 0
        else:
            break
    else:
        pass

print('Thaks for playing ;)')
print('It was nice to have you here')
print('by Jakub Wojciechowski')
