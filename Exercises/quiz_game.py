print("Welcome to quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Ok let's play")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("That answer is not correct!")
    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score+=1
else:
    print("That answer is not correct!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("That answer is not correct!")
print("You got " + str(score) + " questions correct!")