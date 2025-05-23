import math

def main():
    print("Enter the length of two Perpendicular sides to get third side length(hypotenuse)")
    print("hypotenuse side is BC")
    ab:float = float(input("Enter side AB: "))
    ac:float = float(input("Enter side AC: "))
    bc:float = math.sqrt( ab**2 + ac**2)
    print("formula BC**2 = AB**2 + AC**2")
    print(f"The length of BC (hypotenuse) is: {bc} ")

if __name__ == '__main__':
    main()