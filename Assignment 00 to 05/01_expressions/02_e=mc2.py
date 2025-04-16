speed_of_light = 299792458  # speed of light in m/s

def main():
    while True:
        user_input = float(input("Enter mass in kilograms: "))
        if user_input >= 0:
          energy = user_input * speed_of_light ** 2
          print(f"Energy: {energy} Joules")
          break
        else:
          print("Mass cannot be negative.")
          

if __name__ == "__main__":
    main()
    