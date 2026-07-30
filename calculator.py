def calculate(first_number, second_number, operation):
    """Perform a basic arithmetic operation and return the result."""
    if operation == "+":
        return first_number + second_number
    if operation == "-":
        return first_number - second_number
    if operation == "*":
        return first_number * second_number
    if operation == "/":
        if second_number == 0:
            raise ValueError("Division by zero is not allowed.")
        return first_number / second_number
    raise ValueError("Invalid operation. Please choose one of: +, -, *, /")


def main():
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid number input. Please enter numeric values.")
        return

    operation = input("Choose an operation (+, -, *, /): ")

    try:
        result = calculate(first_number, second_number, operation)
    except ValueError as exc:
        print(exc)
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
