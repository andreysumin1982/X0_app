#---- Поле ----
theBoard = {'1':'1', '2':'2', '3':'3',
            '4':'4', '5':'5', '6':'6',
            '7':'7', '8':'8', '9':'9'}

#-------Функция рисует поле с вводимыми в цикле X,0--------------------
def printBoard():
    print(theBoard['1'] + '|' + theBoard['2'] + '|' + theBoard['3'])
    print('-+-+-')
    print(theBoard['4'] + '|' + theBoard['5'] + '|' + theBoard['6'])
    print('-+-+-')
    print(theBoard['7'] + '|' + theBoard['8'] + '|' + theBoard['9'])

#---
def win(who):
    print(f"[VICTORY] -> {who} выйграл!")
    printBoard()
    return exit(0)

#---
def check(turn, who):
    # Проверяем по горизонтали
    if (turn in theBoard['1']) and (turn in theBoard['2']) and (turn in theBoard['3']):
        return True, win(who)
    elif (turn in theBoard['4']) and (turn in theBoard['5']) and (turn in theBoard['6']):
        return True,win(who)
    elif (turn in theBoard['7']) and (turn in theBoard['8']) and (turn in theBoard['9']):
        return True,win(who)
    # Проверяем по вертикали
    elif (turn in theBoard['1']) and (turn in theBoard['4']) and (turn in theBoard['7']):
        return True,win(who)
    elif (turn in theBoard['2']) and (turn in theBoard['5']) and (turn in theBoard['8']):
        win(who)
    elif (turn in theBoard['3']) and (turn in theBoard['6']) and (turn in theBoard['9']):
        return True,win(who)
    # Проверяем по диагонали
    elif (turn in theBoard['1']) and (turn in theBoard['5']) and (turn in theBoard['9']):
        return True,win(who)
    elif (turn in theBoard['3']) and (turn in theBoard['5']) and (turn in theBoard['7']):
        return True,win(who)
    else: return False

#---
def run_X0(move, who):

    #   Проверка на доступность клетки
    # if ('X' in theBoard[move]) or ('O' in theBoard[move]):
    #     print(f"[!] -> Клетка занята")
    #     return f"[!] -> Клетка занята"

        #
    theBoard[move] = who



    #printBoard()
    #print(f"[DRAW] -> Ничья")

#---
if __name__ == '__main__':
    pass
    # printBoard()
    # run_X0()