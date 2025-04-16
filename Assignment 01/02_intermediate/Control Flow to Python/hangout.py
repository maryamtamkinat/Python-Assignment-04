import random

round = 5
def main():
    score = 0
    for i in range(round):
        print("Round", i + 1)

        computer_number: int = random.randint(1, 100)
        your_number: int = random.randint(1, 100)
        print("Your number is ", your_number)

        choice:str = input("Do you think your number is higher or lower than the computer's? ")
        higher_correct:bool = choice == "higher" and your_number > computer_number
        lower_correct:bool = choice == "lower" and your_number < computer_number

        if higher_correct or lower_correct:
            print("You were right. The computer's number was", computer_number)
            score += 1
        else:
            print("You were wrong. The computer's number was", computer_number)
        print("Your score is now", score)
        print()

        print("Thanks for playing!")

if __name__ == "__main__":
    main()