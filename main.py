#socket server 

import socket
import datetime
import os
import sys
#from cryptography.fernet import Fernet

mi_socket = socket.socket()
mi_socket.bind( ('localhost', 8000) )
mi_socket.listen(5)

#mi_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

users = []

def server_interface(): #funcion para generar interfaz en la consola del servidor
    print('SERVIDOR INICIADO')
    print('------------------------------------------------')
    f = open('logs.txt', 'a')
    log = 'New connection established' + str(addr) + str(datetime.datetime.now()) 
    f.write(log)
    f.close()
    
    #encriptar informacion del usuario
    #i = 0
    #key = Fernet.generate_key()
    #fernet = Fernet(key)
    #user = 'User ' + i + ':' +  str(addr)
    #encUser = fernet.encrypt(user.encode())
    #u = open('users.txt', 'a')
    #u.write(encUser)
    #u.close()
    
     

#encriptar archivos de la lista de usuarios antes de meterlos en el txt (provisional)


    
   
while True:
        connection, addr = mi_socket.accept()
        server_interface()
        while True:
            mensaje = input('escriba mensaje ')
            connection.send(str.encode(mensaje))
    
    

    
