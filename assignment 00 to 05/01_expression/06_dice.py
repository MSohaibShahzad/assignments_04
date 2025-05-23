import random

dice:int = 6

def main():
    dice1:int = random.randint(1,dice)
    dice2:int = random.randint(1,dice)
    total:int = dice1 + dice2
    print(f"First die {dice1}, Second die {dice2}")
    print(f"The total of dice 1 and dice 2 is {total}")    



if __name__ == '__main__':
    main()