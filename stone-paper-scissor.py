# Stone Paper Scissor Game
import random
match_count = int(input('Enter the no. of Matches: '))
match_limit = 0
comp_score = 0
user_score = 0
while match_limit < match_count:
    game_option = ['stone', 'paper', 'scissor']
    comp_choice = random.choice(game_option)
    usr_ch = input('Enter: ').lower()
    if usr_ch not in game_option:
        print('Input Error!!!...Try Again!!!')
    else:
        match_limit += 1
        if usr_ch == 'stone':
            if comp_choice == 'scissor':
                print('Computer Choice: ', comp_choice)
                print('You Won!!!')
                user_score += 1
            elif comp_choice == 'paper':
                print('Computer Choice: ', comp_choice)
                print('You Lost')
                comp_score += 1
            elif comp_choice == 'stone':
                print('Computer Choice: ', comp_choice)
                print('Each Gets one Point ')
                comp_score += 1
                user_score += 1
        elif usr_ch == 'paper':
            if comp_choice == 'scissor':
                print('Computer Choice: ', comp_choice)
                print('You Lost')
                comp_score += 1
            elif comp_choice == 'stone':
                print('Computer Choice: ', comp_choice)
                print('You Won!!!')
                user_score += 1
            elif comp_choice == 'paper':
                print('Computer Choice: ', comp_choice)
                print('Each Gets one Point')
                comp_score += 1
                user_score += 1
        elif usr_ch == 'scissor':
            if comp_choice == 'paper':
                print('Computer Choice: ', comp_choice)
                print('You Won!!!')
                user_score += 1
            elif comp_choice == 'stone':
                print('Computer Choice: ', comp_choice)
                print('You Lost')
                comp_score += 1
            elif comp_choice == 'scissor':
                print('Computer Choice: ', comp_choice)
                print('Each gets One Point')
                comp_score += 1
                user_score += 1
print(f'Final Score: Your Score-{user_score}|{comp_score}-Computer Score')
if user_score > comp_score:
    print("Congratulations You Won!!!")
elif user_score == comp_score:
    print("Match Tied...")
else:
    print("Hard Luck, You Lost....Try Again")

