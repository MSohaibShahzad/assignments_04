
def copies(new_list,data,num_copies):
    for i in range(num_copies):
        new_list.append(data)


def main():
    message: str = input("Enter a message: ")
    num_copies: int = int(input("Enter number of copies: "))
    my_list: list = []
    print(f"List before {my_list}")
    copies(my_list,message,num_copies)
    print(f"list after{my_list}")



if __name__ == '__main__':
    main()