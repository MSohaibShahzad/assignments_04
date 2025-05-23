def get_1st_element(list):
    print(list[0])



def create_list():
    my_list : list = []
    user_input = input("Enter the element to  list or click enter to stop: ")
    while user_input != "":
        my_list.append(user_input)
        user_input = input("Enter more elements to list or click enter to stop: ")
    return my_list


def main():
    new_list = create_list()
    get_1st_element(new_list)


if __name__ == '__main__':
    main()