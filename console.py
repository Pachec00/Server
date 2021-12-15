#consola del servidor (archivo de control)
#este archivo forma parte de la estructura del servidor
#este archivo sirve para el manejo del servidor durante la ejecucion

import sys
import os

#lista de comandos
run = 'python main.py'
logs = 'cat logs.txt'
users = 'cat users.txt'

print('Consola del servidor iniciada')

while True:
    command = str(input())

    if command == 'run':
        os.system(run)
    elif command == 'logs':
        os.system(logs)
    elif command == 'users':
        os.system(users)
        
