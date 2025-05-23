
max : int = 10000

def main():
    value1 : int = 0
    value2 : int = 1
    while value1 <= max:        
        value3 = value1
        print(value3)
        value1 = value2
        value2 = value3 + value2
        
       


if __name__ == '__main__':
    main()
