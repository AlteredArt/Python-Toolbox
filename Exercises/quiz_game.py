print("Welcome to quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Ok let's play")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
else:
    print("That answer is not correct!")
    
answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("Correct!")
else:
    print("That answer is not correct!")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print("Correct!")
else:
    print("That answer is not correct!")