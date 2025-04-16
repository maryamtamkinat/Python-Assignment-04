import random

def main():
    for i in range(10):
        random_numbers = random.randint(1, 100)
        print(random_numbers, end=" ")

if __name__ == "__main__":
    main()