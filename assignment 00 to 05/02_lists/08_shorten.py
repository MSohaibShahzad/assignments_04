
max_lenght : int = 5

def pop(list):
    while len(list) > max_lenght:
        list.pop()
    print(list)



def list():
    my_list : list = []
    user_input = input("Enter the elements or press enter to stop: ")
    while user_input != "":
        my_list.append(user_input)
        user_input = input("Enter more element or press enter to stop: ")
    return my_list


def main():
    my_list = list()
    pop(my_list)


    
if __name__ == '__main__':
    main()