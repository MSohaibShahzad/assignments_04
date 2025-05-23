def main():
    print("This program converts from Fahrenheit to Celsius")

    f_temp : float = input("Enter Fahrenheit: ")
    f_temp : float = float(f_temp)
    c_temp : float = (f_temp - 32) * 5.0/9.0
    print(f"Temperature {f_temp}F = {c_temp}C")


if __name__ == '__main__':
    main()