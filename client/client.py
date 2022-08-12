#
import socket
import threading
import os
#
udp_max_size = 1024 # Максимальный размер UDP-пакета
#

def listen(s: socket.socket):
    while True:
        msg = s.recv(udp_max_size)
        print(f"\n{msg.decode()}", sep='\n')
#
def connect(server: str, port: int):
    # создаем socket: (ipv4, udp)
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    name = input('Ваше имя: ')

    # connect
    c.connect((server, port))
    #print(c)
    #
    threading.Thread(target=listen, args=(c,), daemon=True).start()

    # Пишем серверу, что соединились
    c.send('__join'.encode())


    while True:
        msg = input(f"{name}: ")
        c.send(msg.encode())




#
if __name__ == '__main__':
    os.system('clear')
    connect('127.0.0.1', 65000)