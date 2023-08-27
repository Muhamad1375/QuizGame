print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("OK! Let's Play :) ")
score = 0

answer = input("What does cpu stand for? ")

if answer.lower() == "central proccessing unit":
    print('Correct')
    score += 1
else:
    print("Incorrect!")

answer = input("what does GPU satnd for? ")

if answer.lower() == "graphics proccessing unit":
    print('Correct')
    score += 1
else:
    print("Incorrect!")

answer = input("what does RAM stand for? ")

if answer.lower() == "random access memory":
    print('Correct')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")

if answer.lower() == "power supply":
    print('Correct')
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")
