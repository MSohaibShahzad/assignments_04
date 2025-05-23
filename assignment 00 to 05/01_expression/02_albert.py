def main():
    m: float = float(input("Enter kilos of mass: "))
    c: int = 299792458
    e: float = float(m*c**2)
    print("m*c**2")
    print(f"mass = **_{m}_** ")
    print(f"Speed of light: {c} m/s")

    print(f"{e} joules of energy!")

if __name__ == '__main__':
    main()