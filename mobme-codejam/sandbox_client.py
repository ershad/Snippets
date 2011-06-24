#!/usr/bin/python
# client.py
# Author: Ershad K <ershad92@gmail.com>

import socket
import threading
import time
from random import choice
import string


HOST = 'localhost' # localhost / IP of server
PORT = 50008


class Thread(threading.Thread):
    def run(self):
        while True:
                    
            s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s2.connect((HOST, PORT))
            randomString = ''.join([choice(string.ascii_letters) for i in range(8)])
            s2.send('cft ' + randomString)
            d = s2.recv(1024)
            s2.close()
            time.sleep(60)
flag = 0

while True:
    if flag == 0:
        Thread().start()        # Starting the thread
        flag = 1
        
    command = raw_input('>> ')        
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(command)
    data = s.recv(10240)
    s.close()
    print data

