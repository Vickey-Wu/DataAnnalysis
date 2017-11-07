#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2017/10/16 23:30 
# @name: client
# @author：vickey-wu

import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    message = input("-> ")
    while message != 'q':
        s.sendall(bytes(message, "utf-8"))
        data = s.recv(1024)
        print('Received from server: ' + str(data))
        message = input("-> ")
    s.close()

if __name__ == '__main__':
    Main()
