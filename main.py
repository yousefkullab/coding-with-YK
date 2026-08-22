from utils import add_expense, calculate_total, get_highest_expense, get_avg_expense, display_expenses

expenses = [
        {"name": "Food", "amount": 20},
        {"name": "Travel", "amount": 150},
        {"name": "Drink", "amount": 25},
        {"name": "Transport", "amount": 55},
        {"name": "Love", "amount": 90},
        {"name": "Learning", "amount": 170},
        {"name": "Services", "amount": 60}
    ]

if __name__ == "__main__":
    new_expense = {"name": "life-style", "amount": 100}
    add_expense(new_expense, expenses)

    print(f"Total Expeneses: {calculate_total(expenses)}")
    print(f"Highest Expense: {get_highest_expense(expenses)}")
    print(f"AVG Expense: {get_avg_expense(expenses)}")
    display_expenses(expenses)
