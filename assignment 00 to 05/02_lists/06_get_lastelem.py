



def main():
    count : int = -1
    my_list : list = []
    user_input = input("Enter the elements or press enter to stop: ")
    while user_input != "":
        my_list.append(user_input)
        user_input = input("Enter more elements or press enter to stop: ")
        count += 1
    print(f"First element : {my_list[0]}")
    print(f"Last element : {my_list[count]}")



if __name__ == '__main__':
    main()