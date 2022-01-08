#socket server 

import socket
import datetime
import os
import sys

mi_socket = socket.socket()
mi_socket.bind( ('localhost', 8000) )
mi_socket.listen(5)
mi_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


def server_interface():#funcion para generar interfaz en la consola del servidor
    
    print('SERVIDOR INICIADO')
    print('------------------------------------------------')
    
    f = open('logs.txt', 'a')
    log = 'New connection established'  + str(datetime.datetime.now()) 
    f.write(log)
    f.close()
    



def server_connect():
    
    users = 0
    
    while True:
        
        connection, addr = mi_socket.accept()
        
        users = users + 1
        u = open('users.txt', 'a')
        u.write(str(users))
        u.close()
        
        x = datetime.datetime.now()
        d = open('dates.txt', 'a')
        d.write(str(x))
        d.close()
        
        server_interface()
        
        connection.send(str.encode('Bienvenido'))   
        
server_connect()
