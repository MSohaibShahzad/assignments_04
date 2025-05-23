
def save_contact():
    phonebook : dict = {}

    while True:
        name = input("Enter name: ").upper()
        if name == "":
            break

        number = int(input("Enter phone number: "))
        phonebook[name] = number
        print("phone number saved")

    return phonebook
    
def all_contact(phonebook):
    for contacts in phonebook:
        print(contacts, phonebook[contacts])

def search(phonebook):
    while True:
        user_search = input("Enter name to search: ").upper()
        if user_search == "":
            break
        
        if user_search in phonebook:
            print("Contact found!")
            print(user_search, phonebook[user_search])
            
        else:
            print("contact not found")
            

def main():
    phonebook = save_contact()
    all_contact(phonebook)
    search(phonebook)


if __name__ == '__main__':
    main()