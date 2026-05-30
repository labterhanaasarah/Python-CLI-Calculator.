def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b


history = []

while True:
    print("\n====== CALCULATOR ======")
    print("1. Addition +")
    print("2. Subtraction -")
    print("3. Multiplication *")
    print("4. Division /")
    print("5. Show history")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "6":
        print("Exiting program... Goodbye 👋")
        break

    if choice == "5":
        if len(history) == 0:
            print("No operations yet.")
        else:
            for item in history:
                print(item)
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    result = None
    operation = ""

    if choice == "1":
        result = addition(a, b)
        operation = "+"
    elif choice == "2":
        result = subtraction(a, b)
        operation = "-"
    elif choice == "3":
        result = multiplication(a, b)
        operation = "*"
    elif choice == "4":
        result = division(a, b)
        operation = "/"
    else:
        print("Invalid choice")
        continue

    history.append(f"{a} {operation} {b} = {result}")

    print("Result =", result)