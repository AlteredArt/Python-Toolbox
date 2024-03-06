name = input("Type your name: ")
print("Welcome", name, "to your new adventure")

answer = input("You are on a long dark road that forks left and right. Which way should you go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it, or swim across? Type walk to walk around, and swim to swim across").lower()

    if answer == "swim":
        print()
    elif answer == "walk":
        print()
    else:
        print("Not a valid option. You Lose.")

elif answer == "right":
    answer = input("You come to a river, you can walk around it, or swim across? Type walk to walk around, and swim to swim across").lower()


else:
    print("Not a valid option. You Lose.")
