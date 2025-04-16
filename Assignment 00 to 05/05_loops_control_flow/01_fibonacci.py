max_value = 1000

def main():
    a, b = 0, 1
    print(a,b end=", ")
    while True:
        c = a + b
        if c >= max_value:
            break
        print(c, end=", ")
        a, b = b, c

if name == "__main__":
    main()