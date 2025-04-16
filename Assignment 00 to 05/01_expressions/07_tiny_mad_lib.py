def main(noun, verb, adjective):  
    Sentence = f"Once upon a time, there was a {adjective} {noun} who loved to {verb}."

    print(Sentence)

noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")

main(noun, verb, adjective)
