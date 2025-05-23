def main():
    print("This program will check the leap year or not")
    year: int = input("Enter the Year: ")
    year: int = int(year)

    if year % 4 == 0 and year % 100 != 0:
        print("That's a leap year!")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print("That's a leap year!")
    else:
        print("That's not a leap year!")


if __name__ == '__main__':
    main()