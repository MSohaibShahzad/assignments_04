value: int = 200

def main():
    print("This program double it your number until it reach greater than 100")
    user_input: int = int(input("Enter the number: "))
    while user_input < value:
        print(user_input, end=" ")
        user_input : int = user_input * 2
        
if __name__ == '__main__':
    main()