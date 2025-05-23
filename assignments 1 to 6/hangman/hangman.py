from words import words
import random



def get_word(para):
    word = random.choice(para).lower()
    while '-' in word or ' ' in word:
        word = random.choice(para)
    return word


def hangman():
    user_guess = ""
    word : str = get_word(words)
    word_letter : list = list(word)
    guessed_letters: list = []
    display = []
    lives: int = 5
    hint_count: int = 1

    print("Welcome to Hangman Game!")
    print(f"you have lives:{lives} and Hint:{hint_count} ")
    print(f"The word have {len(word)} letters")


    while True:
        display.clear()
        for letter in word_letter:
            if letter in guessed_letters:
                display.append(letter)
            else:
                display.append('_')

        print(" ".join(display))

        if '_' not in display:
            print(f"Congratulations! You guessed the word: {word}")
            break

        if lives == 0:
            print(f"Out of lives! The word was: {word}")
            break
        




        user_guess: str = input("Enter your guess: ").lower()

        if user_guess == "hint":
            if hint_count > 0:
               hint = set(word_letter).difference(set(guessed_letters))
               hint = random.choice(list(hint))
               hint_count -= 1
               print(f"Hint: {hint}")
               continue
            else:
                print("Out of hints!")
                continue
        


        if user_guess in guessed_letters:
            print("You already guessed this Letter")
            continue 

        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Enter single Letter")
            continue 

        
        
        if user_guess in word_letter:
            print("You guessed the right letter")
            guessed_letters.append(user_guess)
        else:
            print("Your guessed Letter is wrong")
            guessed_letters.append(user_guess)     
            lives -= 1
            print(f"lives left: {lives}")
                
hangman()
   

