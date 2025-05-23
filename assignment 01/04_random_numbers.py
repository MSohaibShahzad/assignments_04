# import random

# n_number: int = 10
# min_value: int = 1
# max_value: int = 100

# def main():
#     random_number: int = random.randint(1, 100)
#     while len(random_number) == 10:        
#         print(random_number)
#         random_number: int = random.randint(1, 100)

# if __name__ == '__main__':
#     main()

import random

n_number = 10
min_value = 1
max_value = 100

def main():
    for _ in range(n_number):
        random_number = random.randint(min_value, max_value)
        print(random_number)

if __name__ == '__main__':
    main()
