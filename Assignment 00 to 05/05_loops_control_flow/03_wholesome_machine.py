correct_affirmation = "I am capable of doing anything I put my mind to."

def main():
    while True:
        user_input = input("Please type the following affirmation:" + correct_affirmation)
        if user_input == correct_affirmation:
            print("That's right!")
            break
        else:
            print("That's not right! Please try again.")

if __name__ == "__main__":
    main()
