# Fun Game for Guessing a Number between 1 and 20
import random
secret_num = random.randint(1, 20)
guess_count = 0
guess_limit = 5
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
        break
else:
    print("Sorry You Lost...Try Again!!!!")