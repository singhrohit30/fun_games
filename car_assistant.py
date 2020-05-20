# Your Personal Car Assistant!!!!
print("Welcome! What would you like to Do? ")
command = ""
started = False
while True:
    command = input("Enter your choice ").lower()
    if command == "help":
        print(''' 
1- Enter start to start the Engine
2- Enter stop to stop the Engine 
3- Enter quit to exit ''')
    elif command == "start":
        if started:
            print("Car is already started! ")
        else:
            started = True
            print("Engine Started! Ready to Go!")
    elif command == "stop":
        if not started:
            print("Car is already stopped! ")
        else:
            started = False
            print("Engine Stopped!!")
    elif command == "quit":
        break
    else:
        print("I don't Understand.....")

