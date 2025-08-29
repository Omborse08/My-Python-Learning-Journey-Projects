Note = "Welcome To LoweBudget"
print(Note.center(50))
Line = "================================"
print(Line.center(50))

income = int(input("> Enter Your Monthly Income: "))

rent = int(input("\n> Rent: "))
groc = int(input("> Groceries: "))
inte = int(input("> Internet: "))
tran = int(input("> Transport: "))

total = rent + groc + inte + tran
print("\n> Your total Expenses: ",total)

if rent > groc and rent > inte and rent > tran:
    print("\n> Biggest Expense is:  Rent")
elif groc > inte and groc > tran:
    print("\n> Biggest Expense is:  Groceries")
elif inte > tran:
    print("\n> Biggest Expense is:  Internet")
else:
    print("\n> Biggest Expense is:  Transport")

if total < income:
    remain = income - total
    print("\n> Remaining Balance Is: ",remain)
    print("\n> Great job! You're within your budget.")

elif total > income:
    print("\n> Your Income is",income,"And Your Budget is",total,"Get a Loan Idiot!")

elif total == income:
    print("\n> You spent exactly what you earned.")



