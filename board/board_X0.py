
#---- Поле ----
theBoard = {'top_l':' ','top_m':' ','top_r':' ',
            'mid_l':' ','mid_m':' ','mid_r':' ',
            'low_l':' ','low_m':' ','low_r':' '}

#-------Функция рисует поле с вводимыми в цикле X,0--------------------
def printBoard(board):
    print(board['top_l'] + '|' + board['top_m'] + '|' + board['top_r'])
    print('-+-+-')
    print(board['mid_l'] + '|' + board['mid_m'] + '|' + board['mid_r'])
    print('-+-+-')
    print(board['low_l'] + '|' + board['low_m'] + '|' + board['low_r'])

#---
def win(who):
    print(f"[VICTORY] -> {who} выйграл !")
    printBoard(theBoard)
    return exit(0)

#---
def check(turn, who):
    # Проверяем по горизонтали
    if (turn in theBoard['top_l']) and (turn in theBoard['top_m']) and (turn in theBoard['top_r']):
        win(who)
    elif (turn in theBoard['mid_l']) and (turn in theBoard['mid_m']) and (turn in theBoard['mid_r']):
        win(who)
    elif (turn in theBoard['low_l']) and (turn in theBoard['low_m']) and (turn in theBoard['low_r']):
        win(who)
    # Проверяем по вертикали
    elif (turn in theBoard['top_l']) and (turn in theBoard['mid_l']) and (turn in theBoard['low_l']):
        win(who)
    elif (turn in theBoard['top_m']) and (turn in theBoard['mid_m']) and (turn in theBoard['low_m']):
        win(who)
    elif (turn in theBoard['top_r']) and (turn in theBoard['mid_r']) and (turn in theBoard['low_r']):
        win(who)
    # Проверяем по диагонали
    elif (turn in theBoard['top_l']) and (turn in theBoard['mid_m']) and (turn in theBoard['low_r']):
        win(who)
    elif (turn in theBoard['top_r']) and (turn in theBoard['mid_m']) and (turn in theBoard['low_l']):
        win(who)
    else: return

#---
def run_X0():
    turn = 'X'
    x = 'крестик'
    o = 'нолик'
    who = x
    for i in range(9):
        while True:
            print(f"Ходит {who} '{turn}'")
            move = input()
            # Проверка на доступность клетки и синтаксические ошибки
            try:
                if ('X' in theBoard[move]) or ('O' in theBoard[move]):
                    print(f"[!] -> Клетка занята")
                else: break
            except: print(f"[INFO] -> Неправильно введена клетка"); continue

        theBoard[move] = turn
        check(turn, who)
        if turn == 'X':
            who = o
            turn = 'O'
        else:
            who = x
            turn = 'X'
        printBoard(theBoard)

    else:
        print(f"[DRAW] -> Ничья")

#---
if __name__ == '__main__':
    printBoard(theBoard)
    run_X0()