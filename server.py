#
import socket
import pickle
import os
from board_X0_net import run_X0, printBoard, theBoard, check

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
        if not data: # Если не сообщение, выходим из цыкла
            break
        print(f"Client -> {data}")
        # Вносим изменения в игру от клиента
        run_X0(data, 'O')
        c = check(data, 'O')
        print('check = ', c)
        printBoard()
        # Вносим изиенения в игру от сервера
        msg = input('SRV: ')
        run_X0(msg, 'X')
        # Отправляем клиенту словарь и кодируем его для отправки
        # Словарь(игровое поле)
        board = theBoard
        #client_socket.send(pickle.dumps('test'))
        client_socket.send(pickle.dumps(board))
    # Закрываем соединение
    client_socket.close()
    print(f"[INFO] -> Клиент {address[0]}:{address[1]} отсоединился")


#
if __name__ == '__main__':
    os.system('clear')
    listen('0.0.0.0', 2022)