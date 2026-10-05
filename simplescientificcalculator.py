import math

def show_menu():
    print("\n" + "=" * 40)
    print("        SCIENTIFIC CALCULATOR        ")
    print("=" * 40)
    print("1.  Addition (+)")
    print("2.  Subtraction (-)")
    print("3.  Multiplication (*)")
    print("4.  Division (/)")
    print("5.  Power (x^y)")
    print("6.  Square Root (√x)")
    print("7.  Sine (sin x) [Degrees]")
    print("8.  Cosine (cos x) [Degrees]")
    print("9.  Tangent (tan x) [Degrees]")
    print("10. Natural Logarithm (ln x)")
    print("11. Base-10 Logarithm (log10 x)")
    print("12. Factorial (n!)")
    print("13. Exit")
    print("=" * 40)

def scientific_calculator():
    while True:
        show_menu()
        choice = input("Enter choice (1-13): ").strip()

        if choice == '13':
            print("\nExiting calculator. Goodbye!")
            break

        # Operations requiring two inputs
        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Invalid input. Please enter numerical values.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is undefined.")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            elif choice == '5':
                print(f"Result: {num1} ^ {num2} = {math.pow(num1, num2)}")

        # Operations requiring one input
        elif choice in ('6', '7', '8', '9', '10', '11', '12'):
            try:
                num = float(input("Enter number: "))
            except ValueError:
                print("Error: Invalid input. Please enter a numerical value.")
                continue

            if choice == '6':
                if num < 0:
                    print("Error: Cannot calculate the square root of a negative number.")
                else:
                    print(f"Result: √{num} = {math.sqrt(num)}")

            elif choice == '7':
                rad = math.radians(num)
                print(f"Result: sin({num}°) = {math.sin(rad)}")

            elif choice == '8':
                rad = math.radians(num)
                print(f"Result: cos({num}°) = {math.cos(rad)}")

            elif choice == '9':
                if (num - 90) % 180 == 0:
                    print("Error: Tangent is undefined for this angle.")
                else:
                    rad = math.radians(num)
                    print(f"Result: tan({num}°) = {math.tan(rad)}")

            elif choice == '10':
                if num <= 0:
                    print("Error: Logarithm undefined for zero or negative numbers.")
                else:
                    print(f"Result: ln({num}) = {math.log(num)}")

            elif choice == '11':
                if num <= 0:
                    print("Error: Logarithm undefined for zero or negative numbers.")
                else:
                    print(f"Result: log10({num}) = {math.log10(num)}")

            elif choice == '12':
                if num < 0 or not num.is_integer():
                    print("Error: Factorial requires a non-negative integer.")
                else:
                    print(f"Result: {int(num)}! = {math.factorial(int(num))}")

        else:
            print("Invalid selection. Please choose a number between 1 and 13.")

if __name__ == "__main__":
    scientific_calculator()
