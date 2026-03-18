import pandas as pd
from datetime import datetime
import os

FILE = "expenses.csv"

# load file if it exists
if os.path.exists(FILE):
    df = pd.read_csv(FILE)
else:
    df = pd.DataFrame(columns=["date", "amount", "category", "note"])

while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Monthly total")
    print("4. Exit")

    choice = input("Choose option: ")

    # ADD EXPENSE
    if choice == "1":
        amount = float(input("Amount: "))
        category = input("Category: ")
        note = input("Note: ")

        today = datetime.now().strftime("%Y-%m-%d")

        new_expense = {
            "date": today,
            "amount": amount,
            "category": category,
            "note": note
        }

        df.loc[len(df)] = new_expense
        df.to_csv(FILE, index=False)

        print("Expense added!")

    # VIEW ALL EXPENSES
    elif choice == "2":
        print("\nAll Expenses:")
        print(df)

        total = df["amount"].sum()
        print("Total spent:", total)

    # MONTHLY TOTAL
    elif choice == "3":
        month = input("Enter month (MM): ")

        df["date"] = pd.to_datetime(df["date"])
        monthly = df[df["date"].dt.month == int(month)]

        print("\nExpenses this month:")
        print(monthly)

        print("Total:", monthly["amount"].sum())

    # EXIT
    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid option")