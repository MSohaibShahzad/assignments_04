import random

def main():
    print("I am thinking of a number between 1 to 99")
    number : int = random.randint(1, 99)
    guess_number : int = int(input("Enter your guess: "))

    while guess_number != number:
        if guess_number > number:
            print("Your guess is too high")
        elif guess_number < number:
            print("Your guess is too low")
        

        guess_number: int = int(input("Enter new guess: "))
    print(f"Congrats! The number was {number}")




if __name__ == '__main__':
    main()