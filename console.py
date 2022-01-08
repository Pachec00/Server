import sys
import os


#lista de comandos
#estos comandos no se ejecutan a la vez que el archivo del servidor

run = 'python main.py'
logs = 'cat logs.txt'
help = 'help'
clear = 'clear'
maintenance = 'python maintenance.py'

          
commands = ['run', 'logs','help', 'clear', 'maintenance']

print('Consola del servidor iniciada')
while True:
    command = str(input())

    if command == 'run':
        
        print('')
        os.system(run)
        
    elif command == 'logs':
        
        print('')
        os.system(logs)
        
    elif command == 'help':
        
        for i in range(0, len(commands)):
            print('')
            print(commands[i])
            print('')
            
    elif command == 'clear':
        
        print('')
        os.system(clear)
        print('')
        
    elif command == 'maintenance':
        
        print('')
        #maintenance commands
        print('-users --> Grafica del numero de usuarios')
        print('')
        
        command = str(input())
        
        if command == 'users':
            
            from maintenance import num_users
