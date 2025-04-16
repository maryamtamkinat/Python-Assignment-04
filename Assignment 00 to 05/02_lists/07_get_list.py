def get_first_element(list):
    print(list)

def get_list():
    list = []
    value: str = input("Enter a value: ")
    while value != "":
        list.append(value)
        value = input("Enter a value: ")
    return list

def main():
    list = get_list()
    get_first_element(list)


if __name__ == '__main__':
    main()



    