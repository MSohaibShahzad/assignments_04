import random

r : str = "Rock"
s : str = "scissor"
p : str = "paper"
play : str = ""



def result(user,comp):
    if user == comp:
        print(f"It's tie both choose same")
    elif (user == "r" and comp == "s") or (user == "p" and comp == "r") or (user == "s" and comp == "p"):
        print("You win")
    else:
        print("Sorry you lose")

    if user == "r":
        user = r
    elif user == "s":
        user = s
    else:
        user = p
    
    if comp == "r":
        comp = r
    elif comp == "s":
        comp = s
    else:
        comp = p

    return f"You choose {user} and I choose {comp}"
    


def main():
    print("Let's play Rock Paper scissors\
    press 'r' to choose Rock, 's' for scissors and 'p' for paper")
    user_choice: str = input("Enter your choice: ").lower()
    comp_choice: str = random.choice(["r", "s", "p"])
    while user_choice not in ('r', 's', 'p'):
        user_choice: str = input("press 'r' to choose Rock, 's' for scissors and 'p' for paper: ").lower()
    print(result(user_choice,comp_choice))
    play_again()

def play_again():
    play : str = ""
    while play not in ("yes", "no"):
        play : str = input("Wanna play again(yes/no): ").lower()

    if play == "no" :
        print("Thanks for playing")
    elif play == "yes":
        main()
    


main()