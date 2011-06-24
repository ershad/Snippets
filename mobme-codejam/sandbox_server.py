#!/usr/bin/python
# server.py
# Author: Ershad K <ershad92@gmail.com>

import socket
import os
import commands
import time

HOST = ''
PORT = 50008

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))


while True:
    s.listen(True)
    conn, addr = s.accept()
    data = conn.recv(1024)
    if not data: break

    output = ' '

    if data == 'list':
        output = commands.getoutput('ls')
    elif data == 'pwd':
        output = commands.getoutput('pwd')
    elif data[:3] == 'cat':
        output = commands.getoutput(data)
    elif data == 'time':
        output = time.ctime()  
    elif data[:2] == 'rm':
        outputStatus = os.system(data)
    elif data[:5] == 'touch':
        filename = data.split(' ')[1] #Must be the file name
        finalDataLength = len('touch ' + filename + ' ') #removing the first parts
        finalData = data[finalDataLength:]
        f = open(filename,'w')
        f.write(finalData)
        f.close()
        output = 'The file is successfully written :)'
    else:
        output = 'Invalid command, Please try again.'

    if data[:3] == 'cft':
        timeFileName = data.split(' ')[1]
        fTime = open(timeFileName, 'w')
        fTime.write(time.ctime())
        fTime.close()
        
    conn.send(output)
conn.close()    

print 'Connecetion closed, thank you :)'
