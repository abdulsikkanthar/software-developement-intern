def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print("Temperature Converter Program")
    print("=============================")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    choice = int(input("Enter your choice (1 or 2): "))
    
    if choice == 1:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    elif choice == 2:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
