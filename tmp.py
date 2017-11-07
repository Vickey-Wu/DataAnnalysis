#!/usr/bin/env python
# -*- coding:utf-8 -*-
# socket server.py


#socket通信客户端
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket


def main():
    host = "127.0.0.1"
    port = 5001

    server = ("127.0.0.1", 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = input("-->")
    while message != "q":
        s.sendto(bytes(message, "utf-8"), server)
        data, addr = s.recvfrom(1024)
        print("Received from server: " + str(data))
        message = input("-->")
    s.close()


if __name__ == '__main__':
    main()
