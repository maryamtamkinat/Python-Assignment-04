def main():
    integer1 = int(input("Please enter an integer to be divided: "))
    integer2 = int(input("Please enter an integer to divide by: "))
    quotient = integer1 // integer2
    remainder = integer1 % integer2
    print(f"The reult of this division is {quotient} with a remainder of {remainder}.")
    
main()