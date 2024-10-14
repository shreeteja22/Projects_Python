print("Welcome to My Project.\nTHE ULTIMATE QUIZ GAME")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
    quit()
# name = str(input("Enter your name : "))
# print("Enter your name : ")...............#not necessary that's why removed
print("Let's Play! Quiz on Avengers!")
score = 0

answer = input("1.What is the real name of Thor ? ")
if answer.lower() == 'chris hemsworth':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("2.What is the name of iron man in movie ? ")
if answer.lower() == 'tony stark':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("3.Aunt may is aunt of which avenger? ")
if answer.lower() == 'spiderman':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("4.Steve rogers is referred as whom ? ")
if answer.lower() == 'captain america':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("5.Samuel Jackson played which role? ")
if answer.lower() == 'nick fury':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("6.What is the real name of Doctor strange? ")
if answer.lower() == 'benedict cumberbatch':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("7.What is the name of thor's hammer ? ")
if answer.lower() == 'mjolnir':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Director of Avengers Endgame ? ")
if answer.lower() == 'Russo brothers':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 8) * 100) + "%.")