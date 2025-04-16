import random

def main():
    computer_number = random.randint(1, 10)

    try:
        while True:
            user_value = int(input("Guess a number between 1 and 10: "))

            if user_value == computer_number:
                print("Yay! I guessed your number 🎉")
                break
            elif user_value < computer_number:
                print("Too low!")
            elif user_value > computer_number:
                print("Too high!")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
