
elbonia: int = 16
stanlau: int = 25
mayengua: int =  48

def main():
    print("How old are you? ")
    user_age: int = input("Enter your age: ")
    user_age: int = int(user_age)
    if user_age < 16:
        print(f"You can't vote your age is lower then {elbonia}")
    elif user_age >= 16 and user_age < 25:
        print(f"You can vote in Peturksbouipo where the voting age is {elbonia}.\nYou cannot vote in Stanlau where the voting age is {stanlau}.\nYou cannot vote in Mayengua where the voting age is {mayengua}.")
    elif user_age >= 25 and user_age < 48:
        print(f"You can vote in Peturksbouipo where the voting age is {elbonia}.\nYou can vote in Stanlau where the voting age is {stanlau}.\nYou cannot vote in Mayengua where the voting age is {mayengua}.")
    elif user_age >= 48:
        print(f"You can vote in Peturksbouipo where the voting age is {elbonia}.\nYou can vote in Stanlau where the voting age is {stanlau}.\nYou can vote in Mayengua where the voting age is {mayengua}.")

if __name__ == '__main__':
    main()

# PETURKSBOUIPO_AGE : int = 16
# STANLAU_AGE : int = 25
# MAYENGUA_AGE : int = 48

# def main():
#     # Get the user's age
#     user_age = int(input("How old are you? "))

#     # Check if the user can vote in Peturksbouipo
#     if user_age >= PETURKSBOUIPO_AGE:
#         print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
#     else:
#         print("You cannot vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    
#     # Check if the user can vote in Stanlau
#     if user_age >= STANLAU_AGE:
#         print("You can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
#     else:
#         print("You cannot vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    
#     # Check if user can vote in Mayengua
#     if user_age >= MAYENGUA_AGE:
#         print("You can vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")
#     else:
#         print("You cannot vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")


# # There is no need to edit code beyond this point

# if __name__ == '__main__':
#     main()