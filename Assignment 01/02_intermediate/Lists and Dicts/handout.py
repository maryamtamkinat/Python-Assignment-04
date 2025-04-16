my_list = ["apple", "banana", "orange", "cherry"]
def access_element(index, my_list):
    if 0 <= index < len(my_list):
        return f"Element at index {index}: {my_list[index]}"
    return "Index out of range"

def modify_element(index, new_value, my_list):
    if 0 <= index < len(my_list):
        old_value = my_list[index]
        my_list[index] = new_value
        return f"Element at index {index} modified from {old_value} to {new_value}"
    return "Index out of range"
        
def slice_list(start, end, my_list):
    if 0 <= start < len(my_list) and 0 <= end < len(my_list):
        return f"Sliced list {my_list[start:end]}"
    return "Invalid slice indices"

def list_game():
    print("\n Welcome to the list manipulation")
    my_list = ["apple", "banana", "orange", "cherry"]
    while True:
        print("Current List:", my_list)
        print("1. Access Element")
        print("2. Modify Element")
        print("3. Slice List")
        print("4. Quit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            index = int(input("Enter the index of the element you want to access: "))
            print(access_element(index, my_list))
        elif choice == "2":
            index = int(input("Enter the index of the element you want to modify: "))
            new_value = input("Enter the new value for the modify: ")
            print(modify_element(index, new_value, my_list))
        elif choice == "3":
            start = int(input("Enter the start index for the slice: "))
            end = int(input("Enter the end index for the slice: "))
            print(slice_list(start, end, my_list))
        elif choice == "4":
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 to 4.")

if __name__ == "__main__":
    list_game()