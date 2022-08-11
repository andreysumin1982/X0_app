#
import socket
#
udp_max_size = 1024 # Максимальный размер UDP-пакета
#
def listen(host: str, port: int):
    ''' Ф-ция слушает порт и принимат на вход ip-адрес, порт'''

    # создаем socket: (ipv4, udp)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Привязываю socket к  адресу ()
    s.bind((host, port))
    print(f"[OK] -> Start server..\nListening at {host}:{port}\n")

    # Слушаем порт и клиентов
    clients = []
    flag = True
    while flag:
        msg, addr = s.recvfrom(udp_max_size)
        # Добавляем клиентов
        if addr not in clients:
            clients.append(addr)

        if not msg:
            continue

        # Уведомляем клиентов о подключении
        client_ip = addr[0]
        client_port = addr[1]
        if msg.decode('utf-8') == '__join':
            print(f" [+] -> Клиент {client_ip}:{client_port} присоединился..")
            continue

        msg = f"Клиент {client_ip}:{client_port} - {msg.decode('utf-8')}"
        for client in clients:
            if client == addr:
                continue
            s.sendto(msg.encode('utf-8'), client)
#
if __name__ == '__main__':
    pass