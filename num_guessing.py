import random

top_range = input("Enter a number : ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Please type a number greater than 0")
        quit()
else:
    print("Please type a number next time")
    quit()


random_num = random.randint(0,top_range)
# print(random_num)...............this print the random number!

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type a number next time")
        quit()

    if user_guess == random_num:
        print("You got it right !")
        break
    elif user_guess > random_num:
        print("You are above the number.")
    else:
        print("You are below the number.")

print("You made it in", guesses ,"guesses.")