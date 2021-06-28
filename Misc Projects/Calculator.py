"""Simple calculator taking in user input to perform either addition, subtraction, multiplication or division
NB: subtraction does not return absolute value
"""


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y


print("Operations available are:")
print("1=Add")
print("2=Subtract")
print("3=Multiply")
print("4=Divide")

while True:  # Validating user input and performing chosen operation
    choice = input("What operation would you like to perform? Select 1,2,3 or 4: ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "x", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
        continue
