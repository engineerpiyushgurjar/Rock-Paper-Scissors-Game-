
# RockPaperScissorsGame task form codesoft

import random

user_choice = int(input("Enter your choice : Type 0 for Rock , 1 for Paper , 2 for Scissors. "))

if user_choice >=3 or user_choice < 0:
    print(" You enter invalid number , you lose.  ")

else:
    computer_choice = random.randint (0,2)

print("computer chose : ")
print(computer_choice)

if computer_choice == user_choice :
    print("it's a tie. ")

elif computer_choice > user_choice :
    print("You Lose. ")

elif computer_choice < user_choice :
    print("You Win. ")

elif computer_choice == 0 and user_choice == 2 :
    print("You Lose ")  

elif computer_choice == 2 and user_choice == 0 :
    print("You Lose ")     

print("Thanks for playing!")
print(f"Final Score: You {user_choice} - {computer_choice} Computer")