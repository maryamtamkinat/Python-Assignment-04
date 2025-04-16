import math

def main(AB, AC):
    hypotenuse = AB**2 + AC**2
    result = math.sqrt(hypotenuse)
    print (f"The length of the hypotenuse is: {result}")
user_input1 = float(input("Enter the length of side AB: "))
user_input2 = float(input("Enter the length of side AC: "))
main(user_input1, user_input2)