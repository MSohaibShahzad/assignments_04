import random


def main():
    print("I am thinking a number between 1 to 20")
    guess: int = random.randint(1, 20)
    user_guess = int(input("Enter your guess: "))

    while guess != user_guess:
        if user_guess > guess:
            print("your guess is too high")
        elif user_guess < guess:
            print("your guess is too low")
        user_guess = int(input("Enter your guess again: "))
    print(f"Congrats the number was {guess}")

if __name__ == "__main__":
    main()
