def main():
    print("Simple Calculator (type 'q' to quit)\n")

    while True:
        x = input("Enter first number: ").strip()
        if x.lower() == 'q':
            break

        y = input("Enter second number: ").strip()
        if y.lower() == 'q':
            break

        op = input("Choose operation (+, -, *, /): ").strip()

        # Try converting safely
        try:
            a = float(x)
            b = float(y)
        except ValueError:
            print("Invalid number. Try again.\n")
            continue

        # Perform operation safely
        if op == '+':
            res = a + b
        elif op == '-':
            res = a - b
        elif op == '*':
            res = a * b
        elif op == '/':
            if b == 0:
                print("Error: Division by zero.\n")
                continue
            res = a / b
        else:
            print("Unknown operation. Use +, -, *, or /.\n")
            continue

        # Format result
        if isinstance(res, float) and res.is_integer():
            res = int(res)
        else:
            res = round(res, 6)

        print("Result:", res)
        print()


if __name__ == "__main__":
    main()

