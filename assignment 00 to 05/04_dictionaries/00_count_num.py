

def get_number():
    user_list : list = []   
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
            
        user_input = int(user_input)
        user_list.append(user_input)
    
    return user_list


def count_num(user_list):
    my_dict : dict ={}
    for num in user_list:
        if num in my_dict:
            my_dict[num] += 1
        else:
            my_dict[num] = 1


    return my_dict


def print_count(my_dict):
    for new_dict in my_dict:
        print(f"{new_dict} appears {my_dict[new_dict]} times")
        
    

def main():
    user_numbers = get_number()
    create_dict = count_num(user_numbers)
    print_count(create_dict)

if __name__ == '__main__':
    main()
