
affirmation: str= "I am capable of doing anything I put my mind to"


def main():
    print(f"Please type the following affirmation: {affirmation}")
    user_input:str = input()
    while user_input != affirmation:
        print("That was not the affirmation.")
        print(f"Please type the following affirmation: {affirmation} " )
        user_input:str = input()

    print("That's right!")

if __name__ == '__main__':
    main()