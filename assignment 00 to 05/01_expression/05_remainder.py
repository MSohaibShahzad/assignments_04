
def main():
    print("This program show the result of division and remainder")
    value:int = int(input("Enter the number to divide: "))
    divide_by:int = int(input("Enter a number divide by: "))

    floor_division: int = value // divide_by
    remainder:int = value % divide_by

    print(f"The result of a division is {floor_division} and remainder is {remainder}")



if __name__ == '__main__':
    main()