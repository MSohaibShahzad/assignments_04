import random
def main():
    secret_number = random.randint(1,99)
    print("I am thinking of a number between 1 and 99...")
    user_input = int(input("Enter a guess: "))

    while user_input != secret_number :
        if user_input > secret_number:
            print("your guess is too high")
        elif user_input < secret_number:
            print("Your guess is too low")

        user_input = int(input("Enter a new number: "))
        
    print(f"Congrats! The number was: {secret_number}")
        


if __name__ == '__main__':
    main()