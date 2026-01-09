print("Simple Calculator")
print("=================")
print ("ENTER NUMBERS AND OPERATOR TO PERFORM CALCULATION")
Number1 = int(input("Enter first number: "))
Number2 = int(input("Enter second number: "))
print("CHOOSE OPERATOR + - / * ")
Operator = input("Enter operator: ")

print("=========================================")


if Operator == "+":
    print(Number1 + Number2)
elif Operator == "-":
    print(Number1 - Number2)
elif Operator == "*":
    print(Number1 * Number2)
elif Operator == "/":
    print(Number1 / Number2)
else:
    print("Invalid operator")
