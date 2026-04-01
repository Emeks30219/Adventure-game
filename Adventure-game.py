player_name = input("Type your name:")
print("welcome", player_name, "to this adventure!")

answer= input("You are on a dead road, it has come to an end and you can go left or right. Which way would you want to go? ").lower()

if answer == "left":
     answer = input("You come to a river and you can walk around it or swim across? Type walk to walk around or swim to swim across: ").lower()

     if answer == "swim":
         print("You swam across and were eaten by a crocodile. YOU LOSE! ")

     elif  answer == "walk":
         print("You walked for many miles, ran out of water and lost the game. YOU LOSE! ")
     else:
         print("Not a valid option! You lose. ")
elif answer == "right":
    answer = input("You come to a bridge it looks unstable, do you want cross it or head back (Cross/Back)").lower()

    if answer == "cross":
        answer= input("You cross the bridge and  meet a stranger. Do you talk to them (Yes/No) ").lower()

        if answer == "yes":
            print("You talk to the stranger nicely and they give you Gold and the right directions across the dead end. YOU WIN!")

        elif answer == "no":
            print("You ignore the strangers rudely and they let you die while going the wrong direction. YOU LOSE!")

    elif answer == "back":
        print(" You go back and you lose ")
    else:
        print("Not a valid option! You lose. ")
else:
    print("Not a valid option! You lose. ")
