
def main():
    user_input = input("Enter the number: ")
    curr_value = int(user_input)
    while curr_value < 200:
        print(curr_value)
        curr_value *= 2

if __name__ == '__main__':
    main()