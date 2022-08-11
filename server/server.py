#
import socket
#
udp_max_size = 65000 # Максимальный размер UDP-пакета
#
def listen(host: str='127.0.0.1', port: int=5555):
    ''' Ф-ция слушает порт: 5555 и принимат на вход ip-адрес, порт'''

    # создаем socket: (ipv4, udp)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Привязываю socket к конкретному адресу (127.0.0.1)
    s.bind((host, port))
    print(f"[OK] Start server..\nListening at {host}:{port}")

    # Слушаем порт и клиентов
    clients = []
    while True:
        msg, addr = s.recvfrom(udp_max_size)
        # Добавляем клиентов
        if addr not in clients:
            clients.append(addr)

        # Если сообщение пустое, продолжаем слушать
        if not msg:
            continue

        # Уведомляем клиентов о подключении
        client_id = addr[1]
        if msg.decode('ascii') == '__join':
            print(f"Клиент {client_id} присоединился.")
            continue

#
if __name__ == '__main__':
    listen()