def main(prompt):
    print(f"The parameter of the triangle is {prompt}.")

side1 = int(input("What is the length of side 1: "))
side2 = int(input("What is the length of side 2: "))
side3 = int(input("What is the length of side 3: "))
parameter = (side1 + side2 + side3)
res = main(parameter)