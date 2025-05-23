
min_height: int = 50

def main():
    print("There is minimum height requirenment to ride rollercoaster for safety reasons")
    height: int = input("Enter your height: ")
    height: int = int(height)

    while height != "":
        height: int = int(height)
        if height >= min_height:
            print("Your are tall enough to ride!")
        else:
            print("Your are not tall enough to ride, but maybe next year!")

        height: int = input("Enter your height: ")

if __name__ == '__main__':
    main()