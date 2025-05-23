
inch_in_foot: int = 12

def main():
    print("Feet to inches converter")
    feet: float= float(input("Enter total feet: "))
    inch: float= feet * inch_in_foot
    if feet == 1.0:
        unit = "foot"
    else:
        unit = "feet"
    print(f"The total inches of {feet} {unit} is {inch} inches!")




if __name__ == '__main__':
    main()