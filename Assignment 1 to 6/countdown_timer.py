import time

def countdown_timer():
    seconds = 0

    while True:
        try:
            user_input = int(input("Enter the countdown time in seconds: "))
            if user_input < 0:
                print("Please enter a positive number.")
                continue
            seconds += user_input
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

            for i in range(seconds, 0, -1):
                print(f"Time left: {i} seconds", end="\r")
                time.sleep(1)
            print("Time's up!")