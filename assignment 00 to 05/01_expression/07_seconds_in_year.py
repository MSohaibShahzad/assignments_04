
year_days : int = 365
day_hours : int = 24
hour_min : int = 60
min_sec : int = 60


def main():
    print("Calculate number of seconds in a year")
    input_year: float = float(input("Enter number of year: "))
    total_seconds : float = input_year * year_days * day_hours * hour_min *min_sec
    print(f"There are {total_seconds} seconds in a {input_year}")

if __name__ == '__main__':
    main()