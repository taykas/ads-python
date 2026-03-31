shift = input("Enter your time shift: M – morning, A – afternoon ou N – night: ")

if shift == "M" or shift == "m":
    print("Good Morning!")
elif shift == "A" or shift == "a":
    print("Good Afternoon!")
elif shift == "N" or shift == "n":
    print("Good Night!")
else:
    print("Invalid! Try again")
