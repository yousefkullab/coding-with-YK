from expense import Expense, ExpenseTracker

expense1 = Expense("Food", "Lunch", 50)
expense2 = Expense("Transport", "Taxi", 70)
expense3 = Expense("University", "Book", 90)


tracker = ExpenseTracker()
tracker.add_expense(expense1)
tracker.add_expense(expense2)
tracker.add_expense(expense3)

print("Expenses: ")
tracker.get_expenses()

print(f"Total: {tracker.calculatee_total()}")

taxi_expenses = tracker.filter_expenses("Taxi")
for expense in taxi_expenses:
    print(expense)

tracker.remove_expense(expense1)

print(f"Total: {tracker.calculatee_total()}")
