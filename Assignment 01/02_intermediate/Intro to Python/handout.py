def main():
    print("Welcome to the Planetary Weight Calculator!")
    
    earth_weight = float(input("Enter your weight on Earth (kg): "))
    
    gravity_ratios = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 1.06,
        "Uranus": 0.92,
        "Neptune": 1.19
    }

    print("\nSelect a planet:")
    for planet in gravity_ratios:
        print(f"- {planet}")

    planet = input("Enter the name of the planet: ").title()

    if planet in gravity_ratios:
        new_weight = earth_weight * gravity_ratios[planet]
        print(f"Your weight on {planet} would be: {new_weight:.2f} kg")
    else:
        print("Invalid planet choice. Please try again.")

if __name__ == "__main__":
    main()
