prompt = "What do you want?"
joke = """Why don't programmers like nature? \n Because it has too many bugs! 😆"""
sorry = "Sorry I only tell jokes."

def main():
    user_input = input(prompt)
    user_input = user_input.strip().lower()
    if "joke" in user_input:
        print(joke)
    else:
        print(sorry)

if __name__ == "__main__":
    main()
