def sum(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def arithmetic_operations(a, b, operation):
    if operation.lower() == "a":
        print(f"Sum: {sum(a, b)}")
    elif operation.lower() == "s":
        print(f"Subtract: {subtract(a, b)}")
    elif operation.lower() == "m":
        print(f"Multiply: {multiply(a, b)}")
    elif operation.lower() == "d":
        print(f"Divide: {divide(a, b)}")
    else:
        print("Invalid operation")

def printOperationResults():
    arithmetic_operations(10, 5, "a")
    arithmetic_operations(10, 5, "s")
    arithmetic_operations(10, 5, "m")
    arithmetic_operations(10, 5, "d")

printOperationResults()
