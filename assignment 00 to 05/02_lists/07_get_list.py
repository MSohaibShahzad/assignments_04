def main():
    my_list : list = []
    user_input = input("Enter the elements or press enter to stop: ")
    while user_input != "":
        my_list.append(user_input)
        user_input = input("Enter more elements or press enter to stop: ")

    print(f"list = {my_list}")

if __name__ == '__main__':
    main()