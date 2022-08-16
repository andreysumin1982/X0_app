#
import socket
import pickle
import os
from board_X0_net import additem, printBoard, theBoard, check, check_draw
#
def listen(host: str, port: int):
    #создаем socket: (ipv4, tcp)
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Привязка
    server.bind((host, port))
    # Слушаем порт
    server.listen()
    print(f"[OK] -> Start server..\nListening at {host}:{port}\n")
    # Принимаем отправл. запросы от клиентов
    global client_socket
    client_socket, address = server.accept()
    # Уведомление о подключении клиентов
    if address:
        print(f" [+] -> Клиент {address[0]}:{address[1]} присоединился")
    while True:
        # Получаем запрос и декодируем в читаемый вид
        data = client_socket.recv(4096).decode('utf-8')
        print(f"Client -> {data}")
        # Вносим изменения в игру от клиента
        additem(data, 'O')
        # Проверяем на выйгрыш
        if check('O', 'нолик'):
            printBoard()
            print(f"[VICTORY] -> нолик выйграл!")
            # Отправляем клиенту и кодируем сообщение
            client_socket.send(pickle.dumps(f"[VICTORY] -> нолик выйграл!"))
            break
        # проверка на ничью
        if check_draw() == 9:
            print(f"[DRAW] -> Ничья")
            # Отправляем клиенту и кодируем сообщение
            client_socket.send(pickle.dumps(f"[DRAW] -> Ничья"))
            break
        # Выводим игровое поле
        printBoard()
        # Вносим изиенения в игру от сервера
        msg = input('SRV: ')
        additem(msg, 'X')
        # Проверяем на выйгрыш
        if check('X', 'крестик'):
            printBoard()
            print(f"[VICTORY] -> крестик выйграл!")
            # Отправляем клиенту и кодируем сообщение
            client_socket.send(pickle.dumps(f"[VICTORY] -> крестик выйграл!"))
            break
        # проверка на ничью
        if check_draw() == 9:
            print(f"[DRAW] -> Ничья")
            # Отправляем клиенту и кодируем сообщение
            client_socket.send(pickle.dumps(f"[DRAW] -> Ничья"))
            break
        # Отправляем клиенту словарь(игровое поле) и кодируем его
        board = theBoard
        client_socket.send(pickle.dumps(board))
    # Закрываем соединение при завершении цыкла
    close_connect(address)
#
def close_connect(address):
    print(f"[INFO] -> Клиент {address[0]}:{address[1]} отсоединился")
    client_socket.close()
    server.close()
#
if __name__ == '__main__':
    os.system('clear')
    listen('0.0.0.0', 2022)