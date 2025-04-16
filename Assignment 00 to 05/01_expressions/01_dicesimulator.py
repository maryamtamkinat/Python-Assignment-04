import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"Total of the two dice: {total}")

def main():
    die1 : int = 10
    print(f"die1 in main() start as:" + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"die1 in main() end as:" + str(die1))

if __name__ == "__main__":
    main()