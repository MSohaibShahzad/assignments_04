import random

dice_side : int = 6

def roll_dice():
    dice1: int = random.randint(1,dice_side)
    dice2: int = random.randint(1,dice_side)
    total: int = dice1 + dice2
    print(f"Total of two dices: {total}")

def main():
    die1: int = 10
    print("Roll dices three times")
    roll_dice()
    roll_dice()
    roll_dice()
    



if __name__ == '__main__':
    main()