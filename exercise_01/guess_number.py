from random import randint

def guessing_game():
    answer = randint(1, 100)
    while True:
        guessable_number = int(input("Guess a number between 1 and 100: "))
        if guessable_number == answer:
            print(f"Guessed number is {answer}. Congratulations! You guessed correctly!")
            break
        if guessable_number < answer:
            print("Too low!")
        else:
            print("Too high!")


guessing_game()