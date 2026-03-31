num1 = float(input("Enter number one: "))
num2 = float(input("Enter number two: "))

op = input("Enter the operation (+ - % *): ")

if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == "%":
    if num2 == 0:
        print("Division for zero it's not possible") 
    print(f"{num1} % {num2} = {num1 / num2}")
else:
    print(f"{num1} * {num2} = {num1 * num2}")