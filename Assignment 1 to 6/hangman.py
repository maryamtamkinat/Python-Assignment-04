import random

word_list = ["python", "hangman", "challenge", "programming", "computer"]
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
        display  += " "
    return display

def hangman():
    word = random.choice(word_list)
    guessed_letters = set()
    attempts = 6
    while attempts > 0:
        print("Welcome to Hangman!")
        print("Word:", display_word(word, guessed_letters))
        print(f"Guessed Letter: {" ".join(guessed_letters)}")
        print(f"Attempts left: {attempts}")
    
        guess = input("Guess a letter: ").lower()
        guessed_letters.add(guess)  
    
        if guess in word:
            print("Good guess")
        else:
            print("Wrong guess")
            attempts -= 1 
    
            if "_" not in display_word(word, guessed_letters):
                print(f"Congratulation! You Guessed the word: {word} 🎉")
                break

hangman()