import random


def main():
    count = 0
    while count != 10:
        value : int = random.randint(1, 100)
        count += 1
        print(value, end=" ")
    
if __name__ == '__main__':
    main()