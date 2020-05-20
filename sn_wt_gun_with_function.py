# Snake water Gun using Function
import random


def sn_wt_gun(usr_ch):
    global comp_score
    global user_score
    if usr_ch == 'snake':
        if comp_choice == 'water':
            print(comp_choice)
            print('You Won!!!')
            user_score += 1
        elif comp_choice == 'gun':
            print(comp_choice)
            print('You Lost')
            comp_score += 1
        elif comp_choice == 'snake':
            print(comp_choice)
            print('Each Gets one Point ')
            comp_score += 1
            user_score += 1
    elif usr_ch == 'water':
        if comp_choice == 'snake':
            print(comp_choice)
            print('You Lost')
            comp_score += 1
        elif comp_choice == 'gun':
            print(comp_choice)
            print('You Won!!!')
            user_score += 1
        elif comp_choice == 'water':
            print(comp_choice)
            print('Each Gets one Point')
            comp_score += 1
            user_score += 1
    elif usr_ch == 'gun':
        if comp_choice == 'snake':
            print(comp_choice)
            print('You Won!!!')
            user_score += 1
        elif comp_choice == 'water':
            print(comp_choice)
            print('You Lost')
            comp_score += 1
        elif comp_choice == 'gun':
            print(comp_choice)
            print('Each gets One Point')
            comp_score += 1
            user_score += 1


match_count = int(input('Enter the no. of Matches: '))
match_limit = 0
comp_score = 0
user_score = 0
while match_limit < match_count:
    game_option = ['snake', 'water', 'gun']
    comp_choice = random.choice(game_option)
    usr_ch = input('Enter: ').lower()
    if usr_ch not in game_option:
        print('Input Error!!!...Try Again!!!')
    else:
        match_limit += 1
        sn_wt_gun(usr_ch)
print(f'Final Score: Your Score {user_score}|{comp_score}-Computer Score')
if user_score > comp_score:
    print("Congratulations You Won!!!")
elif user_score == comp_score:
    print("Match Tied...")
else:
    print("Hard Luck, You Lost....Try Again!!!")
