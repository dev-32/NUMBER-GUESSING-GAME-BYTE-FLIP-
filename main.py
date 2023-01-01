import random

ans = int(random.randint(1, 101))

status = True
trial = 5
print("<<<<____NUMBER GUESSING GAME____>>>>")
print("A number is chosen between 1 to 100. Guess the number within 5 Trials")
print("__________ALL THE BEST__________\n")
while status and trial != 0:
    comp = int(random.randint(1, 101))
    try:
        player = int(input("player : "))
    except:
        print("Please enter the correct value!!")
    if player == ans:
        print("You won the game Congrats!!")
        break
    elif player > ans:
        print(f"The number is less than {player}.")
    else:
        print(f"The number is greater than {player}.")
    print("Computer : ")
    if comp == ans:
        print("Computer wins")
        break
    trial -= 1
    if trial == 0 and player != ans and comp != ans:
        print("You both have exhausted trials.")
        print(f"The number was {ans}")
        print("Do you want to play again? (Y/N) : ")
        what = input()
        if what == "Y":
            trial = 5
            ans = random.randint(1, 101)
        else:
            break
print("<<<_____THANK YOU_____>>>")