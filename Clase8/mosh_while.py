# weight = int(input('Enter your weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == 'L':
#     converted = weight*0.45
#     print(f'You are {converted} kilos')
# else:
#     converted = weight/0.45
#     print(f'You are {converted} pounds')

# GAME
# numAdivinar == 89
# chances == 3
# Entrar un numero
# Mientras el numero sea diferente de numAdivinar
# print 'Entre un numero de dos cifras'
# si entra el numAdivinar print 'Winner' and exit
# Reducir chances by 1
# else prompt 'Sorry you failed'

# numAdivinar = 89
# chancesCount = 0
# chancesLimit = 3
# while chancesCount < chancesLimit:
#     numero = int(input('Entre un numero de dos cifras: '))
#     chancesCount += 1
#     if numero == numAdivinar:
#         print(f'Winner, {numAdivinar} is the right number')
#         break
# else:
#     print('Sorry you failed')


# GAME2
# Description: at prompt the program is ready for you to enter a command if you type help you get a list of commands that the car supports:
# start - to start the car / print Car started - ready to go
# stop - to stop the car / print Car stopped.
# quit - to exit / program terminates

# any other commands that you type the program should tell the user that it doesn't understand the command

# Algoritmo
# prompt > until something is typed
# If input is help then prompt the menu on lines 35-37
# If start is entered then print line 35
# If stop is entered then print line 36
# If quit then break
# else type line 39

# from pickle import TRUE
# from tkinter import FALSE


# action = ""
# started = FALSE
# while True:
#     action = input('> ').lower()
#     if action == 'start':
#         if started:
#             print("Hey don't start the car twice")
#         else:
#             print("Car started - Ready to go")
#             started = True
#     elif action == 'stop':
#         if not started:
#             print("Hey don't stop the car twice")
#         else:
#             print('Car stopped.')
#             started = False
#     elif action == 'help':
#         print("""
# start - to start the car')
# stop - to stop the car')
# quit - to exit
#         """)
#     elif action == 'quit':
#         break
#     else:
#         print('I do not understand that command.')
