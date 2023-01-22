import random

def game():
    print("Welcome to my number guessing game!")
    upper = "str"
    valid = False
    while valid == False:
        try:
            upper = int(input("What's the maximum value of the number?"))
            valid = True
        except ValueError:
            print("you did not input a number. Try again.")
    guess = -1
    answer = random.randint(1,upper)
    while guess != answer:
        guess = guesser()
        if guess < answer:
            print("Your guess was smaller than the actual number")
        elif guess > answer:
            print("Your guess was larger than the actual number")
    print("Congratulations! You won the game!")

def guesser():
    validguess = False
    while validguess == False:
        try:
            attempt = int(input("Guess a number:"))
            validguess = True
        except ValueError:
            print("you did not input a number. Try again.")
    return attempt


game()