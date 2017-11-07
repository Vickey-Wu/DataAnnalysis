#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2017/11/4 23:08 
# @name: tmp2
# @author：vickey-wu


#服务器端
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket


def main():
    host = "127.0.0.1"
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server started")
    while True:
        data, addr = s.recvfrom(1024)
        print("Message from: " + str(addr))
        print("From connected user: " + str(data))
        # data =  str(data).upper()
        if str(data) == "hello":
            print("Sending: " + str(data))
            s.sendto(bytes(str(data), "utf-8"), addr)
        # else:
        #     s.sendto(bytes(str(data), "utf-8"), addr)
    s.close()


if __name__ == '__main__':
    print("socket server running...")
    main()


