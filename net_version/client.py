#
import socket
import os
import pickle
#
def printBoard(theBoard):
    print(theBoard['1'] + '|' + theBoard['2'] + '|' + theBoard['3'])
    print('-+-+-')
    print(theBoard['4'] + '|' + theBoard['5'] + '|' + theBoard['6'])
    print('-+-+-')
    print(theBoard['7'] + '|' + theBoard['8'] + '|' + theBoard['9'])
#
def connect(server: str, port: int):
    # создаем socket: (ipv4, tcp)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to server
    client.connect((server, port))
    while True:
        # Отправляем сообщение
        client.send(input('Client: ').encode('utf-8'))
        # Получаем сообщение (словарь)
        msg = client.recv(4096)
        data = pickle.loads(msg)
        if type(data) == dict: # Проверяем пришедшие данные
            print(f"SRV -> {printBoard(data)}")
        else:
            print(f"SRV -> {data}")
            break
    client.close()
#
if __name__ == '__main__':
    os.system('clear')
    connect('127.0.0.1', 2022)