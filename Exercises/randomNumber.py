import random

print("Guess the random number: ")
top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time. ")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesess = 0
# r = random.randrange(-5, 11)

# print(random_number)
while True:
    guesess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time')
        continue
    if user_guess == random_number:
        print("You got it correct")
        break
    elif user_guess > random_number:
        print("You were above the number.")
    else:
        print("You were below the number.")



print("You got it in" , guesess, "guesses!")