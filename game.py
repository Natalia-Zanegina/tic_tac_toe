def Show_Matrix(m):
    print()
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=' ')
        print()
    print()

def Steps(sign, player):
    global matrix
    print('Ход игрока за {}.'.format(sign))
    step_row = int(input('Введите номер строки: '))
    step_column = int(input('Введите номер столбца: '))
    while matrix[step_row][step_column] != '*':
        print('Ошибка! Эта позиция уже занята.')
        step_row = int(input('Введите номер строки: '))
        step_column = int(input('Введите номер столбца: '))
        
    matrix[step_row][step_column] = sign

    if step_row == 0:
        player.add(str(step_column))
    elif step_row == 1:
        player.add(str(step_column + len(matrix)))
    else:
        player.add(str(step_column + 2*len(matrix)))
    
    Show_Matrix(matrix)

def Checking(player):
    global winning_combinations
    for i in winning_combinations:
        if i.issubset(player):
            return True
    return False

matrix = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
Show_Matrix(matrix)

winning_combinations = [{'0', '1', '2'}, {'3', '4', '5'}, {'6', '7', '8'}, {'0', '3', '6'}, {'1', '4', '7'}, {'2', '5', '8'}, {'0', '4', '8'}, {'2', '4', '6'}]

sign_x = 'X'
sign_0 = '0'
player_X = set()
player_0 = set()

for i in range(5):
    Steps(sign_x, player_X)
    if Checking(player_X):
        print('Победили крестики!')
        break
    else:
        if i != 4:
            Steps(sign_0, player_0)
            if Checking(player_0):
                print('Победили нолики!')
                break
        else:
            print('Ничья!')