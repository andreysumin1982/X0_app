#
import socket
from board_X0_net import theBoard
from board_X0_net import printBoard
import json
import pickle
#
udp_max_size = 1024 # Максимальный размер UDP-пакета
#
# def listen(host: str, port: int):
#     ''' Ф-ция слушает порт и принимат на вход ip-адрес, порт'''
#
#     # создаем socket: (ipv4, udp)
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
#     # Привязываю socket к  адресу ()
#     s.bind((host, port))
#     print(f"[OK] -> Start server..\nListening at {host}:{port}\n")
#
#     # Слушаем порт и клиентов
#     clients = []
#     while True:
#         msg, addr = s.recvfrom(udp_max_size)
#         #print(msg, addr)
#
#         # Уведомление о подключении клиентов
#         if msg.decode() == '__join':
#             print(f" [+] -> Клиент {addr[0]}:{addr[1]} присоединился")
#
#             # Добавляем клиентов в список
#             if addr not in clients:
#                 clients.append(addr)
#             print(addr)
#             print(clients)
#             continue
#
#         if not msg: # Если пустое сообщение
#             continue
#         #s.sendto(printBoard().encode(), addr)
#
#         msg = f"Клиент {addr[0]} прислал сообщение:\n-> {msg.decode()}"
#
#         #b = printBoard().decode()
#         for client in clients:
#             #print(client)
#             if client == addr: # Не отправлять данные клиенту, который их прислал
#                 continue
#             # Отправляем сообщение
#             s.sendto(msg.encode(), client)

def listen(host: str, port: int):
    #создаем socket: (ipv4, tcp)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Привязка
    server.bind((host, port))
    # Слушаем порт
    server.listen()
    print(f"[OK] -> Start server..\nListening at {host}:{port}\n")
    # Принимаем отправл. запросы от клиентов
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

        print(printBoard())
        # Вносим изиенения в игру от сервера
        msg = input('SRV: ')

        # Отправляем клиенту словарь и кодируем его для отправки
        board = theBoard
        client_socket.send(pickle.dumps(board))
    # Закрываем соединение
    client_socket.close()
    print(f"[INFO] -> Клиент {address[0]}:{address[1]} отсоединился")


#
if __name__ == '__main__':
    listen('0.0.0.0', 2022)