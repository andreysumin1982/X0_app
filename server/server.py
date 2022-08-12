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
        #print(msg, addr)

        # Уведомление о подключении клиентов
        client_ip = addr[0]
        client_port = addr[1]
        if msg.decode() == '__join':
            print(f" [+] -> Клиент {client_ip}:{client_port} присоединился")

            # Добавляем клиентов в список
            if addr not in clients:
                clients.append(addr)
            # print(clients)
            continue

        if not msg: # Если пустое сообщение
            continue

        msg = f"Клиент {client_ip} прислал сообщение:\n-> {msg.decode()}"

        for client in clients:
            #print(client)
            if client == addr: # Не отправлять данные клиенту, который их прислал
                continue
            # Отправляем сообщение
            s.sendto(msg.encode(), client)

#
if __name__ == '__main__':
    pass