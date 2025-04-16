def main(prompt):
    inches = prompt * 12
    print (f"{prompt} feet is equal to {inches} inches.")
user_input = float(input("Enter the number of feet: "))
main(user_input)
