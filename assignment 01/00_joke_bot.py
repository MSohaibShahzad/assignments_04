
prompt: str = "What do you want? "
joke: str = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
sorry: str = "Sorry I only tell jokes."


def main():
    if user_input == "joke":
        print(joke)
    else:
        print(sorry)

user_input = input(prompt).lower()

if __name__ == '__main__':
    main()
