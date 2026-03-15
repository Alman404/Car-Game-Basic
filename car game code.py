command = ""


print('GAME HAS STARTED, WRITE "start" to initialize the game')

while command.lower() != "quit":

    command  = input('').lower()

    if command.lower() == 'start':

        print('Game has started')

    elif command.lower() == 'stop':

        print('Game has stopped')


    elif command  == 'help':

        print(""" 

        - Press start to initiate the game 
        - Press stop to hold the game
        - Press help to get the gamne guide

""")
     
    else:

        print('Write something we can work ON!!!')