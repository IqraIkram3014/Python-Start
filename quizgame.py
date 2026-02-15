#Quiz Game
print("Hey! Welcome to my quiz game!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()


print("Let's Play! ")
score = 0

answer = input("What is CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is GPU stands for? ")
if answer.lower() == "general processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is ROM stands for? ")
if answer.lower() == "read only memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " in your questions!")
print("You got " + str((score/4) * 100) + " %")