def count_numbers():
    count_dicts = {}

    while True:
        num = input("Enter a number (or Exit to quit): ")
        if num.title() == "Exit":
            break
        if num.isdigit():
            count_dicts[num] = count_dicts.get(num, 0) + 1
        else:
            print("Invalid input. Please enter a number or Exit.")
    
    return count_dicts  # <-- Yeh ab loop ke bahar hai

def display_count(count_dicts):
    print("\nNumber counts:")
    for key, value in count_dicts.items():
        print(f"{key} appears {value} times")

if __name__ == "__main__":
    counts = count_numbers()
    display_count(counts)
