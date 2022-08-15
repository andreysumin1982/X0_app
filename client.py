#
import requests
import socket
import threading
import os

#
udp_max_size = 1024 # Максимальный размер UDP-пакета
#


# def receive(s: socket.socket):
#     while True:
#         msg = s.recv(udp_max_size)
#         print(f"\n{msg.decode()}", sep='\n')
# #
# def connect(server: str, port: int):
#     # создаем socket: (ipv4, udp)
#     c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
#     name = input('Ваше имя: ')
#
#     # connect
#     c.connect((server, port))
#     #print(c)
#     #
#     threading.Thread(target=receive, args=(c,), daemon=True).start()
#
#     # Пишем серверу, что соединились
#     c.send('__join'.encode())
#
#     while True:
#         msg = input(f"{name}: ")
#         #print(f"Отрпавка сообщения - {msg}")
#         c.send(msg.encode())

        #c.send(board.encode())



# def recive(s: socket.socket):
#     # Получаем сообщение
#     while True:
#         msg = s.recv(udp_max_size)
#         print(f"\n[*]{msg.decode()}", sep='\n')
# #
#
# #
# def connect(server: str, port: int):
#     # создаем socket: (ipv4, udp)
#     global c
#     c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
#     name = input('Ваше имя: ')
#
#     # connect
#     c.connect((server, port))
#     #print(c)
#     #
#     threading.Thread(target=recive, args=(c,), daemon=True).start()
#
#     # Пишем серверу, что соединились
#     c.send('__join'.encode())
#
#     # Подкл. доску
#     board_X0.printBoard()
#
#     while True:
#         msg = input(f"{name}: ")
#         reply(msg)
#         #c.send(msg.encode())
#     # msg = input(f"{name}: ")
#     # reply(msg)
#     #board_X0.run_X0()
#
# def reply(msg):
#     # отправляем сообщение
#
#     c.send(msg.encode())

def connect(server: str, port: int):
    # создаем socket: (ipv4, tcp)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to server
    client.connect((server, port))
    while True:
        # Отправляем сообщение
        client.send(input('Client: ').encode('utf-8'))
        # Получаем сообщение
        msg = client.recv(1024).decode('utf-8')
        print(f"SRV -> {msg}")




#
if __name__ == '__main__':
    os.system('clear')
    connect('127.0.0.1', 2022)