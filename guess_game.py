# Fun Game for Guessing a Number between 1 and 20
import random

while True:
    # gettin a random number between 1-20 from random module
    secret_num = random.randint(1, 20)

    guess_count = 0

    # we can set number of attempts or take it as input from user

    # guess_limit = 5
    # uncomment the line below to take input from the user & comment the upper line

    guess_limit = int(input('Enter the Number of attempts: '))


    while guess_count < guess_limit:

        given_num = int(input("Enter: "))
        # print(secret_num)
        guess_count += 1
        if given_num > secret_num:
            print("You Entered a greater number...You have ", guess_limit - guess_count, "Chances left")
        elif given_num < secret_num:
            print("You Entered a Smaller number...You have ", guess_limit - guess_count, "Chances left")
        elif given_num == secret_num:
            print("Congratulations....YOU Have WON!!!")
            exit()
    else:
        print("Sorry You Lost...Try Again!!!!")

        choice = input('Press Y to play again or Q to exit ').lower()
        
        if choice == 'y':
            continue
        else:
            print('THANK YOU FOR PLAYING WITH US....HOPE TO SEE YOU AGAIN!!!')
            exit()