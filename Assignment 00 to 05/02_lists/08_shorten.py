max_length = 3

def shorten(list):
    while len(list) > max_length:
        remove = list.pop()
        print(remove)

def get_list():
    list = []
    user_input = input("Enter a value: ")
    while user_input != "":
        list.append(user_input)
        user_input = input("Enter a value: ")
    return list

def main():
    list = get_list()
    shorten(list)

if __name__ == "__main__":
    main()  # Brackets lagana mat bhoolna
