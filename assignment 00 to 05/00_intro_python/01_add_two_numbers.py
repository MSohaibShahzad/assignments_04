def main():
    print("This program adds two numbers.")

    num1 = input("Enter first number: ")
    num1 : int = int(num1)
    num2 = input("Enter second number: ")
    num2 : int = int(num2)
    total: int = num1 + num2
    print(f"The total of {num1} and {num2} is {total}.")



if __name__ == '__main__':
    main()