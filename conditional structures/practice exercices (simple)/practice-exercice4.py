salary = float(input("Enter your salary: "))

if salary < 5.000:
    print(f"your allowance for the end of the year is: {salary*0.15}")
else:
    print(f"your allowance for the end of the year is: {salary*0.10}")