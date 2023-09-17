# SImple car game which runs with help of commands
command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "help":
        print('''
01 - "Start"---> to start the car.
02 - "Stop"---> to stop the car.
03 - "Quit"---> to quit the game.
''')
    elif command == "start":
        if started:
            print("Car is already running.")
        else:
            started = True    
            print("Car Started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False;
            print("Car stopped.")    
    elif command == "quit":
        print("exit.")
        break;
    else:
        print("sorry! i didn't understand that") 