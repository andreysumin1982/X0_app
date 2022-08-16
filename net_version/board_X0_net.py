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
        return True #win(who)
    elif (turn in theBoard['4']) and (turn in theBoard['5']) and (turn in theBoard['6']):
        return True #win(who)
    elif (turn in theBoard['7']) and (turn in theBoard['8']) and (turn in theBoard['9']):
        return True #win(who)
    # Проверяем по вертикали
    elif (turn in theBoard['1']) and (turn in theBoard['4']) and (turn in theBoard['7']):
        return True #win(who)
    elif (turn in theBoard['2']) and (turn in theBoard['5']) and (turn in theBoard['8']):
        return True #win(who)
    elif (turn in theBoard['3']) and (turn in theBoard['6']) and (turn in theBoard['9']):
        return True #win(who)
    # Проверяем по диагонали
    elif (turn in theBoard['1']) and (turn in theBoard['5']) and (turn in theBoard['9']):
        return True #win(who)
    elif (turn in theBoard['3']) and (turn in theBoard['5']) and (turn in theBoard['7']):
        return True #win(who)
    else: return False

#
def check_draw():
    x, o, count = 'X', 'O', 0
    for value in theBoard.values():
        if (x in value) or (o in value):
            count+=1
    return count

#
def additem(move, who):
    theBoard[move] = who

#
if __name__ == '__main__':
    pass
    print(check('O'))