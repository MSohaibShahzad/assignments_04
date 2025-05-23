
sentence: str = "Panaversity is fun. I learned to program and used Python to make my"

def main():
   adjective: str = input("Please Enter an adjective: ")
   noun: str = input("Enter a noun: ")
   verb: str = input("Enter a verb: ")

   print(f"{sentence} {adjective} {noun} {verb}!")

if __name__ == '__main__':
    main()