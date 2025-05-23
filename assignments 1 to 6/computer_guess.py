import random

def guess():
    value1: int = 1
    value2: int = 1000
    user = ""
    guess = 0

    while user != "c":
        if value1 == value2:
            print(f"You are trying to confuse me but I know your number is {comp_guess}")

        comp_guess : int = random.randint(value1,value2)

        user : str = input(f"The number is {comp_guess} If guess is high(h), for low (l) and for correct(c): ")
        
        while user not in ("h", "l", "c"):
             user = input(f'The number is {comp_guess} type alphabet If guess is high press "h", if low press "l" and if correct press "c": ')   

        if user == "h" or "l" or "c":
            if user == "h":
                value2 = comp_guess
            elif user == "l":
                value1 = comp_guess

        guess += 1
    
    print(f"I found it! Your number was {comp_guess} after {guess} tries!")

guess()
