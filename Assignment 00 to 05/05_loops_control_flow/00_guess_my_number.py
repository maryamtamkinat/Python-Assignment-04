import random

def main():
    secret = random.randint(1, 99)
    guess = int(input("Enter a guess: "))
    print("I'm thinking of a number between 0 and 99.")
    while True:
        if guess < secret:
            print("Yout guess is too low")
        elif guess > secret:
            print("Your guess is too high")
        else:
            print(f"Congrats! The number was: {secret}")
            break
        
        guess = int(input("Enter a new number: "))

if __name__ == "__main__":
    main()