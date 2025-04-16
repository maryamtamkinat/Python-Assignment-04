def main():
    fahrenheit = float(input("Enter the number in fahrenheit: ")) 
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    message : str = (f"Temperature {fahrenheit}F = {celsius}C")
    print (message)

if __name__ == "__main__":
    main()