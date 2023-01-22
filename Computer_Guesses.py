import random

def game():
    print("Welcome to my other guessing game!")
    print("This time, you'll think of an integer and the computer will try to guess it")
    validinput = False
    while validinput == False:
       try:
           answer = int(input("What is the integer you have in mind?"))
           validinput = True
       except ValueError:
           print("You did not input an integer.")
    guess = 0.1
    lower = 1
    upper = 10
    while guess != answer:
        try:
            guess = random.randint(lower,upper)
        except ValueError:
            lower -= 2
            upper += 2
        print(f"My guess is {guess}.")
        feedback = input(f"Is {guess} too high (H), too low(L), or correct (C)?").lower()
        if feedback == "h":
            upper = guess - 1
        if feedback == "l":
            lower = guess + 1
        while feedback not in {"h","l","c"}:
            print("Not a valid input. try again.")
            feedback = input(f"Is {guess} too high (H), too low(L), or correct (C)?").lower()
    print(f"Yay, I guessed your number {answer}!")


game()