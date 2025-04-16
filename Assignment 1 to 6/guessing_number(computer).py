import random

def main():
    user_value = input("Enter your secret number between 1 and 10.")
    guess = random.randint(1, 10)
    print(f"Computer guess is {guess}")

    while True:
        feedback = input("is this correct guess? (low / high / correct)").lower()
        if feedback == "correct":
            print(f"Yay! I guessed your number: {guess} 🎉")
            break
        elif feedback == "low":
            print("Too low!")
        elif feedback == "high":
            print("Too high!")
        else:
            print("Invalid feedback. Please enter 'low', 'high', or 'correct'.")
            continue

        guess = random.randint(1, 10)
        print(f"Computer new guess is {guess}")


if __name__ == "__main__":
    main()
