# 💸 Expense Tracker

A command-line expense tracker built in Python. It lets you log daily expenses, view your spending history, and check monthly totals — all saved to a CSV file so your data persists between sessions.

---

## Features

- Add expenses with amount, category, and a note
- View all recorded expenses with a running total
- Filter expenses by month to see monthly spending
- Auto-saves data to a CSV file (`expenses.csv`)

---

## How It Works

1. On startup, the program loads existing expenses from `expenses.csv` (or creates a fresh one if it doesn't exist)
2. A menu is shown with options to add, view, or filter expenses
3. Every new entry is immediately saved to the CSV
4. The loop keeps running until the user chooses to exit

---

## Menu Options

| Option | Action |
|---|---|
| 1 | Add a new expense (amount, category, note) |
| 2 | View all expenses and total amount spent |
| 3 | View expenses for a specific month |
| 4 | Exit the program |

---

## CSV Structure

Data is stored in `expenses.csv` with the following columns:

| Column | Description |
|---|---|
| `date` | Auto-filled with today's date (YYYY-MM-DD) |
| `amount` | Expense amount |
| `category` | e.g. Food, Transport, Shopping |
| `note` | Short description of the expense |

---

## Code Structure

| Part | Description |
|---|---|
| File load block | Reads existing CSV or creates empty DataFrame |
| `choice == "1"` | Captures input, builds a new row, appends and saves |
| `choice == "2"` | Prints full DataFrame and sum of all amounts |
| `choice == "3"` | Filters rows by month using datetime parsing |
| `choice == "4"` | Breaks the loop and exits |

---

## Concepts Used

| Concept | Where Used |
|---|---|
| `pandas` (DataFrame) | Storing and manipulating expense data |
| `os.path.exists()` | Checking if the CSV file already exists |
| `pd.read_csv()` / `df.to_csv()` | Reading and saving data to CSV |
| `datetime.now()` | Auto-filling today's date |
| `pd.to_datetime()` | Parsing dates for month filtering |
| `dt.month` | Extracting month from date column |
| `df.loc[len(df)]` | Appending a new row to the DataFrame |
| `while True` + `break` | Keeping the menu loop running until exit |
| `float(input())` | Taking numeric input from user |

---

## Requirements

Install the required library before running:

```bash
pip install pandas
```

---

## How to Run

```bash
python expense_tracker.py
```

---

## Sample Output

```
Expense Tracker
1. Add expense
2. View expenses
3. Monthly total
4. Exit
Choose option: 1
Amount: 250
Category: Food
Note: Lunch at cafe
Expense added!
```
