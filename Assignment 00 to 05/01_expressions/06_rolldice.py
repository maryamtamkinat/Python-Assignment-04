import random

dice = 6
def main():
    dice1 = random.randint(1, dice)
    dice2 = random.randint(1, dice)
    total = dice1 + dice2
    print(f"Total of {dice1} and {dice2} is: {total}")

main()
    